from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class ListAuth(permissions.BasePermission):
    def has_permission(self, request, view: View):
        SAFE_METHODS = ("POST", "HEAD", "OPTIONS")
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_seller or request.user.is_superuser


class IsSellerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_seller or request.user.is_superuser


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_seller
