from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
    Check if user is Super User
    """
    def has_permissions(self, request, view):
        return self.request.user.is_superuser()

class IsHost(permissions.BasePermission):
    """
    Check if user is Host
    """
    def has_permissions(self, request, view):
        return hasattr(self.request.user, 'host')

class IsClient(permissions.BasePermission):
    """
    Check if user is Client
    """
    def has_permissions(self, request, view):
        return hasattr(self.request.user, 'client')
