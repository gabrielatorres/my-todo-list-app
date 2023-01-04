from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import createNewTask, createNewProject

# Create your views here.


def index(request):
    title = 'Welcome to Django Course'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = '@gabrielatorres'
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    return HttpResponse('<h2>Hello %s </h2>' % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })
    # return JsonResponse(projects, safe=False)


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    # return HttpResponse('tasks: %s' % task.title)


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': createNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': createNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')
