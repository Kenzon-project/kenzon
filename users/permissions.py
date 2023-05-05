from rest_framework import permissions
import ipdb

class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user.is_staff != obj.is_staff or request.user == obj)