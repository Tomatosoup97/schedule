from rest_framework import serializers

from .models import BasicUser, ClientProfile, HostProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicUser
        fields = (
            'id', 'last_login', 'username', 'password', 'first_name',
            'last_name', 'email', 'date_joined', 'is_staff', 'is_active',
            'groups', 'user_permissions', 'host', 'client')
        read_only_fields = (
            'last_login','date_joined', 'is_staff',
            'is_active', 'user_permissions', 'groups',
            'host', 'client')

class ClientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClientProfile
        fields = ('id', 'user')

class HostProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = HostProfile
        fields = ('id', 'user')