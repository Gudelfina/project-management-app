from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_list(request):
    project = Project.objects.all()
    context = {
        "projects": project,
    }
    return render(request, "projects/list.html", context)
