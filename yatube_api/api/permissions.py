from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if (
            request.user.is_authenticated
            or request.method in permissions.SAFE_METHODS):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
