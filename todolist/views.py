from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from todolist.models import Task
from .forms import NewTaskForm
from django.http.response import JsonResponse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    todo_list = Task.objects.filter(user=request.user)
    context = {
    'username': username,
    'todo_list': todo_list,
 
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = Task()
            new_task.user = request.user
            new_task.date = datetime.datetime.now()
            new_task.title = form.cleaned_data['title']
            new_task.description = form.cleaned_data['description']
            new_task.is_finished = False

            new_task.save()
            return redirect('todolist:show_todolist')
    else:
        form = NewTaskForm()

    context = {'form': form}
    return render(request, 'create_task.html', context)

def update_task(request, id):
    task = Task.objects.get(pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")

def add_task(request):
    if request.method == 'POST':
        new_task = Task()
        new_task.user = request.user
        new_task.date = datetime.datetime.now()
        new_task.title = request.POST.get('title')
        new_task.description = request.POST.get('description')
        new_task.is_finished = False

        new_task.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# Bonus Tugas 6
def delete_task_ajax(request, id):
    if request.method == 'DELETE':
        task = Task.objects.get(pk = id)
        task.delete()
        return HttpResponse(b"DELETED", status=201)

    return HttpResponseNotFound()