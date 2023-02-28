from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskList,CreateTaskViewSet,DeleteTaskViewSet,AssignTaskViewSet,CompleteTaskViewSet

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/create', CreateTaskViewSet.as_view(), name='task-create'),
    path('tasks/asign', AssignTaskViewSet.as_view(), name='task-asign'),
    path('tasks/complete', CompleteTaskViewSet.as_view(), name='task-complete'),
    path('tasks/delete', DeleteTaskViewSet.as_view(), name='task-delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)