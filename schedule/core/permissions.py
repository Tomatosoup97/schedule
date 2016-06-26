from rest_framework import permissions

class IsSafeMethod(permissions.BasePermission):
    """
    Returns if request is GET, OPTIONS or HEAD
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS

class IsChange(permissions.BasePermission):
    """
    Returns if request is PUT or PATCH
    """
    def has_permission(self, request, view):
        POST_PATCH = ['PUT', 'PATCH']
        return request.method in POST_PATCH

class IsPOST(permissions.BasePermission):
    """
    Returns if request is POST
    """
    def has_permission(self, request, view):
        return request.method == "POST"

class IsDELETE(permissions.BasePermission):
    """
    Returns if request is DELETE
    """
    def has_permission(self, request, view):
        return request.method == "DELETE"

def IsFields(*fields):
    class IsFieldPermission(permissions.Base):
        _fields = set(fields)

        def has_permission(self, request, view):
            return set(request.data.keys()) <= self._fields

        def has_object_permission(self, request, view, obj):
            return set(request.data.keys()) <= self._fields

    return IsFieldPermission