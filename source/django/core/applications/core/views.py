from django.shortcuts import render


def home(request):
    context = {
        "title": "AvantKeel"
    }
    return render(request, 'core/home.html', context)