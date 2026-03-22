from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def homePage(request):
    return HttpResponse('<h1>Welcome to Home page</h1><a href="/app/">Go to application</a>')

def applicationPage(request):
    return HttpResponse("main application page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage),
    path('app/' ,applicationPage)
]
