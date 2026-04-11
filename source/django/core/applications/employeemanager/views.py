from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Team


@login_required
def teambase(request):
    teams = Team.objects.all()
    return render(request, "employeemanager/teambase.html", {
        "teams": teams
    })


@login_required
def create_team(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        Team.objects.create(
            name=name,
            description=description,
            submitted_by=request.user
        )

    return redirect("/app")
