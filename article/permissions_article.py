from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'you are not a owner of the object ! '

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
