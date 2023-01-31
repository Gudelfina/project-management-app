from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.


@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=task)
    context = {
        "form": form,
        "task_object": task,
    }
    return render(request, "tasks/edit.html", context)


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {"form": form}

    return render(request, "tasks/create.html", context)


@login_required
def task_list(request):
    task = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": task,
    }
    return render(request, "tasks/list.html", context)
