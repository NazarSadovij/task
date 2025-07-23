from django.urls import path
from task_app import views
urlpatterns = [
    path('', views.TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>/detail', views.TaskDetailView.as_view(), name="task_detail"),
    path('task/create', views.TaskCreareView.as_view(), name="task_create"),
]