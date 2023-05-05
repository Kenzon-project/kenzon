from rest_framework import permissions
import ipdb

class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return request.user.is_authenticated and request.user.is_admin or request.user.is_authenticated and request.user == obj
        return request.user.is_authenticated and request.user.is_admin and obj.is_admin == False or request.user == obj

class UserPermissionCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin