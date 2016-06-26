from rest_framework import permissions

from calendars.models import Meeting

class IsSuperUser(permissions.BasePermission):
    """ Check if user is Super User """
    def has_permission(self, request, view):
        return request.user.is_authenticated() and \
                request.user.is_superuser

class IsHost(permissions.BasePermission):
    """ Check if user is Host """
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated() and hasattr(user, 'host')

class IsClient(permissions.BasePermission):
    """ Check if user is Client """
    def has_permission(self, request, view):
        return user.is_authenticated() and hasattr(request.user, 'client')