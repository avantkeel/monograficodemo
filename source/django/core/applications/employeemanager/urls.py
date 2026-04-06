from django.urls import path
from .views import employeemanager

urlpatterns = [
    path("", employeemanager, name="employee"),
]