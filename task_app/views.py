from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from task_app.models import Task
from .forms import TaskForm



class TaskListView(LoginRequiredMixin, ListView):
    model=Task
    template_name = "task_list.html"

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name="task_detail.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_update.html"
    form_class = TaskForm
    success_url = reverse_lazy('task_list')