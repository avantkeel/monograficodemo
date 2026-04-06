from django.urls import path
from .views import hello_view, employee,signup

urlpatterns = [
    path('hello/', hello_view),
    path('employee',employee),
    path('v1/auth/signup', signup)  # type: ignore # todo fix
]
