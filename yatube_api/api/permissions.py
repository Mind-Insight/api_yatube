from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            request.method not in permissions.SAFE_METHODS
            and obj.author != request.user
        ):
            return False
        return True
