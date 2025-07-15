from django.shortcuts import render
from django.views.generic import ListView

from task_app.models import Task

# Create your views here.
class TaskListView(ListView):
    model=Task
    template_name = "Track/task_list.html"





    