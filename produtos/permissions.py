from rest_framework import permissions


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated and request.user.is_seller


class IsSellerOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
        if request.method in SAFE_METHODS:
            return True
        else:
            return (
                request.user.is_authenticated
                and request.user.is_seller
                and obj.user == request.user
            )
