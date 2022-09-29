from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {
    'username': request.user,
    'list_barang': data_todolist,
    'nama': 'Yeira',
    'id': '2106751726',
    'last_login': request.COOKIES['last_login'],
    'task_count': data_todolist.count()
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        task = Task(
            title = request.POST.get('task'),
            description = request.POST.get('description'),
            date = datetime.datetime.now(),
            user = request.user,
            is_finished = False)
        task.save()
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')

def delete(request, id):
    deletion = Task.objects.filter(id=id)
    deletion.delete()
    return redirect('todolist:show_todolist')

def change(request, id):
    change = Task.objects.get(id = id)
    change.is_finished = not(change.is_finished)
    change.save()
    return redirect('todolist:show_todolist')