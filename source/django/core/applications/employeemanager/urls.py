from django.urls import path
from .views import teambase, create_team,delete_team

urlpatterns = [
    path("", teambase, name="teambase"),
    path("createteam/", create_team, name="createteam"),
    path("delete-team/<int:team_id>/", delete_team, name="delete_team"),
]
