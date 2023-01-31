from django.urls import path
from projects.views import (
    project_list,
    show_project,
    create_project,
    edit_project,
)

urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("edit/<int:id>/", edit_project, name="edit_project"),
]
