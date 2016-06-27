from rest_framework import permissions
from users.permissions import IsClient, IsHost

class IsPublic(permissions.BasePermission):
    """
    Check if meeting is public
    Nested object inspection allowed
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'public'):
            return obj.public
        return obj.meeting.public

class IsPrivate(permissions.BasePermission):
    """
    Check if meeting is private
    Nested object inspection allowed
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'private'):
            return obj.private
        return obj.meeting.private

class IsMeetingClient(IsClient):
    """
    Check if client is meeting's client
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.clients.filter(id=user.id):
            return True
        return False

class IsMeetingHost(IsHost):
    """
    Check if user is meeting's host.
    Nested object inspection allowed
    """
    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'hosts'):
            if obj.hosts.filter(id=user.id):
                return True
            return False
        # Nested inspection
        if obj.meeting.hosts.filter(id=user.id):
            return True
        return False