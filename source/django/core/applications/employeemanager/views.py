from django.shortcuts import render
from applications.employeemanager.server.handlers.employeeHandler import employeeHandler

def employeemanager(request):
    return render(request, "employeemanager/employeemanager.html", {
        "title": "AvantKeel"
    })
