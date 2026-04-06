from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from utils.adapters.httpAdapter import Request , Response
from .handler.hello.HelloHandler import HelloHandler
from .models import User
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError


employees = []


def handleSignup(req: Request, res: Response):
    try:
        # 1. Basic validation (ensure keys exist)
        data = req.body
        required_fields = ["username", "email", "firstname", "lastname", "password"]
        if not all(k in data for k in required_fields):
            res.json({"success": False, "message": "Missing fields"}, status=400)
            return

        # 2. Create user and HASH the password
        new_user = User(
            username=data["username"],
            email=data["email"],
            firstname=data["firstname"],
            lastname=data["lastname"],
            # make_password handles the PBKDF2 hashing for you
            passwordhash=make_password(data["password"]) 
        )
        
        new_user.save()

        # 3. Build response from the ACTUAL saved object
        myResponse = {
            "success": True,
            "message": "Account created successfully",
            "data": {
                "user": {
                    "id": new_user.id,
                    "username": new_user.username,
                    "email": new_user.email,
                }
            }
        }
        res.json(myResponse, status=201)

    except IntegrityError:
        # This catches duplicate usernames/emails based on your model constraints
        res.json({
            "success": False, 
            "message": "Username or Email already exists"
        }, status=409)
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        res.json({
            "success": False, 
            "message": "An internal error occurred"
        }, status=500)




    


@csrf_exempt
def signup(request):
    if request.method == "POST":
        req = Request(request);
        res = Response()
        try:
            # body = json.loads(request.body)
            answare = handleSignup(req,res)

            return JsonResponse(res.data,status=res.status)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)













@csrf_exempt
def hello_view(request):
    req = Request(request)
    res = Response()
    HelloHandler(req, res)
    return JsonResponse(res.data, status=res.status)


def createEmployee(body):
    client_data = {
        "id": len(employees) + 1,
        "first_name": body.get("first_name"),
        "last_name": body.get("last_name"),
        "email": body.get("email"),
        "role": body.get("role"),
    }

    employees.append(client_data)
    return client_data


def viewEmployee():
    return employees


def deleteEmployee(emp_id):
    global employees

    for emp in employees:
        if emp["id"] == emp_id:
            employees = [e for e in employees if e["id"] != emp_id]
            return True

    return False  # if not found


@csrf_exempt
def employee(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            new_employee = createEmployee(body)

            return JsonResponse({
                "message": "Employee created successfully",
                "employee": new_employee
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

    elif request.method == "GET":
        return JsonResponse({
            "employees": viewEmployee()
        })

    elif request.method == "DELETE":
        emp_id = request.GET.get("id")

        if not emp_id:
            return JsonResponse({
                "error": "Employee id is required"
            }, status=400)

        try:
            emp_id = int(emp_id)
        except ValueError:
            return JsonResponse({
                "error": "Invalid id format"
            }, status=400)

        deleted = deleteEmployee(emp_id)

        if not deleted:
            return JsonResponse({
                "error": "Employee not found"
            }, status=404)

        return JsonResponse({
            "message": f"Employee {emp_id} deleted successfully"
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)
