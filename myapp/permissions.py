from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Client').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Employee').exists()

class CanCreateTask(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and IsClient().has_permission(request, view)

class CanDeleteTask(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and IsManager().has_permission(request, view)

class CanEditTask(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and IsManager().has_permission(request, view)


class CanCompleteTask(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and IsEmployee().has_permission(request, view)


class CanAssignTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        return IsManager().has_permission(request, view) and obj.created_by.groups.filter(name='Employee').exists()
