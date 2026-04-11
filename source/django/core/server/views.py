# ⚠️ Deprecated module
# This code is no longer maintained.
# Do not use for new features.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from utils.adapters.httpAdapter import Request , Response
from .handler.hello.HelloHandler import HelloHandler
from .handler.signup.SignUpHandler import handleSignup
from .handler.health import HealthHandler
employees = []

def execute(fun,request):
    """⚠️ Deprecated module"""
    req = Request(request)
    res = Response()
    fun(req, res)
    return JsonResponse(res.data, status=res.status)

@csrf_exempt
def signup(request):
    """⚠️ Deprecated module"""
    return execute(handleSignup, request) if request.method == "POST" else JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def hello_view(request):
    """⚠️ Deprecated module"""
    return execute(HelloHandler,request)

@csrf_exempt
def health(request):
    """⚠️ Deprecated module"""
    return execute(HealthHandler,request)
