from rest_framework import permissions
from users.permissions import IsClient, IsHost

class IsPublic(permissions.BasePermission):
    """ Check if meeting is public """
    def has_object_permission(self, request, view, obj):
        return obj.public

class IsPrivate(permissions.BasePermission):
    """ Check if meeting is private """
    def has_object_permission(self, request, view, obj):
        return obj.private

class IsMeetingClient(IsClient):
    """ Check if client is meeting's client """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.clients.filter(id=user.id):
            return True
        return False

class IsMeetingHost(IsHost):
    """ Check if host is meeting's host """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.hosts.filter(id=user.id):
            return True
        return False