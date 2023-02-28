from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsClient, IsManager, IsEmployee, CanCreateTask, CanDeleteTask, CanAssignTask,CanCompleteTask

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        else:
            return Task.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user:
            return Task.objects.all()
        else:
            return Task.objects.filter(created_by=user)

class CreateTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanCreateTask, IsClient]
    queryset = Task.objects.all()
        
class CompleteTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanCompleteTask, IsEmployee]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        task = Task.objects.get(title = title)
        task.status = 'Complete'
        task.save()
        return Response({"Response":"Task updated successfully"})

class DeleteTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanDeleteTask, IsManager]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        Task.objects.get(title = title).delete()
        
        return Response({"Response":"Task deleted successfully"})    

class AssignTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanAssignTask, IsManager]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        assigned = serializer.validated_data['assignee_name']
        task = Task.objects.get(title = title)
        task.assigned = assigned
        task.save()
        return Response({"Response":"Task assigned successfully"})    

