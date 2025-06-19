from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="tasks"),
    path('create/', TaskCreateView.as_view(), name="create"),
    path('<int:pk>/<slug:slug>/', TaskDetailView.as_view(), name='task'),
    path('update/<int:pk>/<slug:slug>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/<slug:slug>/', TaskDeleteView.as_view(), name='delete'),
]