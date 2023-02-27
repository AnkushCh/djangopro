from rest_framework.permissions import BasePermission, SAFE_METHODS

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
        return request.method == 'DELETE' and IsManager().has_permission(request, view)

class CanAssignTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        return IsManager().has_permission(request, view) and obj.created_by.groups.filter(name='Employee').exists()
