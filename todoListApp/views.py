from django.shortcuts import redirect, render, get_object_or_404
from . import forms, models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    tasks = models.taskForm.objects.all().filter(user = request.user)
    total_tasks = models.taskForm.objects.filter(user = request.user).count()
    completed_tasks = models.taskForm.objects.filter(user = request.user, completed = True).count()
    if request.method == 'GET':
        return render(request, 'home.html',{
            'form' : forms.createTasksForm,
            'tasks' : tasks,
            'total' : total_tasks,
            'completed' : completed_tasks
        })
    else:
        task = models.taskForm.objects.create(task_name = request.POST['task_name'], user = request.user)
        return redirect('/')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/')
            except:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    'error': 'Usuario existente'
                })
        else:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:

            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': "El usuario o contraseña es incorrecto"
            })
        else:
            login(request, user)
            return redirect('/')
        
    

@login_required 
def delete_task(request, id):
    task = get_object_or_404(models.taskForm, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

@login_required
def completed_task(request, id):
    task = get_object_or_404(models.taskForm, id=id)
    if request.method == 'POST':
        task.completed = True
        task.save()
        return redirect('/')

