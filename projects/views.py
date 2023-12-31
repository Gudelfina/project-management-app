from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

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


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.owner = request.user
            receipt.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create.html", context)


@login_required
def edit_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("show_project", id=id)
    else:
        form = ProjectForm(instance=project)
    context = {
        "form": form,
        "project_object": project,
    }
    return render(request, "projects/edit.html", context)
