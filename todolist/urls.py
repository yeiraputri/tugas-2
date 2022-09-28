from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import create_task
from todolist.views import logout_user
from todolist.views import delete
from todolist.views import change

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout_user'),
    path('delete/<int:id>', delete, name='delete'),
    path('change/<int:id>', change, name='change'),

]