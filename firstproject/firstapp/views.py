from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project
import datetime as dt


def homepage(request):
    return render(request, 'firstapp/temp0.html')


def display(request):
    return HttpResponse("<h1>My First Heading</h1>")


def displaydatetime(request):
    d = dt.datetime.now()
    s = "<b>Current Date and Time: </b>"+str(d)
    return HttpResponse(s)


def template(request):
    return render(request, 'firstapp/temp1.html', {"name": "Aman"})


def index(request):
    return render(request, 'firstapp/index.html')


def listProject(request):
    projectList = Project.objects.all()
    return render(request, 'firstapp/listProject.html', {'projects': projectList})


def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'firstapp/addProject.html', {'form': form})
