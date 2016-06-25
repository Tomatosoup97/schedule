from rest_framework import permissions

class IsSafeMethod(permissions.BasePermission):
    """
    Returns if request is GET, OPTIONS or HEAD
    """
    def has_permissions(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsChange(permissions.BasePermission):
    """
    Returns if request is PUT or PATCH
    """
    def has_permissions(self, request, view):
        PUT_PATCH = ['PUT', 'PATCH']
        return request.method in post_patch

class IsPOST(permissions.BasePermission):
    """
    Returns if request is POST
    """
    def has_permissions(self, request, view):
        return request.method == "POST"

class IsDELETE(permissions.BasePermission):
    """
    Returns if request is DELETE
    """
    def has_permissions(self, request, view):
        return request.method == "DELETE"