from django.contrib import admin
from django.urls import path
from django.shortcuts import render  # Import render instead of HttpResponse
from applications.core.views import home
from applications.account.views import signup, signin

def applicationPage(request):
    # If you have an app-specific page, render it here too
    return render(request, 'pages/app.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('app/', applicationPage),
    path('signup/',signup),
    path('signin/',signin)
]