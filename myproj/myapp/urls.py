from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskList, TaskDetail,CreateTaskViewSet,EditTaskViewSet,DeleteTaskViewSet

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/create', CreateTaskViewSet.as_view(), name='task-create'),
    path('tasks/edit', EditTaskViewSet.as_view(), name='task-edit'),
    path('tasks/delete', DeleteTaskViewSet.as_view(), name='task-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)