from rest_framework import permissions


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_seller
