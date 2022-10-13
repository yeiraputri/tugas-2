from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>', update_task, name='update-task'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:id>', delete_task_ajax, name='delete_task_ajax'),
]