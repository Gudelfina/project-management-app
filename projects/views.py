from django.shortcuts import render, get_object_or_404
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def project_list(request):
    project = Project.objects.filter(owner=request.user)
    context = {
        "projects": project,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project = Project.objects.get(id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/detail.html", context)
