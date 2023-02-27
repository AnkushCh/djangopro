from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsClient, IsManager, IsEmployee, CanCreateTask, CanDeleteTask, CanAssignTask,CanCompleteTask,CanEditTask
# @api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def protected_view(request):

from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanCreateTask | CanDeleteTask | CanAssignTask | CanCompleteTask]

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
    # permission_classes = [IsAuthenticated, CanDeleteTask | CanAssignTask | CanCompleteTask]
    permission_classes=[AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user:
            return Task.objects.all()
        else:
            return Task.objects.filter(created_by=user)
        
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == 'complete':
            instance.completed_by = self.request.user
            instance.save()

class CreateTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,CanCreateTask]

    # def post(self,request):
    #     serializer = self.serializer_class(data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #     email = serializer.validated_data['email']
    #     otp = serializer.validated_data['otp']
    #     new_password = serializer.validated_data['new_password']

    #     if User.objects.filter(email = email).exists():
    #         user = User.objects.get(email = email)
    #         if user.otp == otp:
    #             user.password = make_password(new_password)
    #             user.save()
    #             return Response({"Response":"password updated successfully"})  
    #         else:
    #             return Response({"Response":"Otp did not match"})  
    #     else: 
    #         return Response({"Error":"email does not exists"})
        
class EditTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanEditTask]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            if user.otp == otp:
                user.password = make_password(new_password)
                user.save()
                return Response({"Response":"password updated successfully"})  
            else:
                return Response({"Response":"Otp did not match"})  
        else: 
            return Response({"Error":"email does not exists"})

class DeleteTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanDeleteTask]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            if user.otp == otp:
                user.password = make_password(new_password)
                user.save()
                return Response({"Response":"password updated successfully"})  
            else:
                return Response({"Response":"Otp did not match"})  
        else: 
            return Response({"Error":"email does not exists"})
    

class CompleteTaskViewSet(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, CanCompleteTask]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            if user.otp == otp:
                user.password = make_password(new_password)
                user.save()
                return Response({"Response":"password updated successfully"})  
            else:
                return Response({"Response":"Otp did not match"})  
        else: 
            return Response({"Error":"email does not exists"})
    