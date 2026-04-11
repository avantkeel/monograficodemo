from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Team


@login_required
def teambase(request):
    teams = Team.objects.filter(submitted_by=request.user)
    return render(request, "employeemanager/teambase.html", {
        "teams": teams
    })

@login_required
def team_workspace(request, team_id):
    team = get_object_or_404(Team, id=team_id, submitted_by=request.user)

    return render(request, "employeemanager/workspace.html", {
        "team": team
    })

@login_required
def delete_team(request, team_id):
    if request.method == "POST":
        Team.objects.filter(id=team_id, submitted_by=request.user).delete()

    return redirect("/app/")

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
    return redirect("/app/")