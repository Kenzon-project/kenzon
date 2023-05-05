from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class ListAuth(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_seller or request.user.is_superuser


class IsSellerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_seller or request.user.is_superuser
