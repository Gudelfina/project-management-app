from django.urls import path
from tasks.views import create_task, task_list, edit_task

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", task_list, name="show_my_tasks"),
    path("edit/<int:id>/", edit_task, name="edit_task"),
]
