from django.urls import path
from task_app import views
urlpatterns = [
    path('', views.TaskListView.as_view(), name="task_list")
    path('', views.DetailView.as_view(), name="task_detail)
]