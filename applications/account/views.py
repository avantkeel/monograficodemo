from django.shortcuts import render

def signup(request):
    context = {
        "title": "AvantKeel"
    }
    return render(request, 'signup.html', context)

def signin(request):
    context = {
        "title": "AvantKeel"
    }
    return render(request, 'signin.html', context)
