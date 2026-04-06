from django.urls import path
from .views import hello_view, signup, health

urlpatterns = [
    path('hello/', hello_view),
    path('v1/auth/signup', signup),  # type: ignore # todo fix
    path('v1/health', health)
]
