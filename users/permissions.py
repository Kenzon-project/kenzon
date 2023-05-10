from rest_framework import permissions


class UserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return request.user.is_authenticated and request.user.is_admin
        return (
            request.user.is_authenticated
            and request.user.is_admin
            and obj.is_admin == False
            or request.user == obj
        )


class UserPermissionCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ("POST", "HEAD", "OPTIONS")
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated and request.user.is_admin
