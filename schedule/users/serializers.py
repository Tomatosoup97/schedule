from rest_framework import serializers

from .models import BasicUser, ClientProfile, HostProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicUser
        fields = (
            'id', 'last_login', 'username', 'first_name',
            'last_name', 'email', 'date_joined',)
        read_only_fields = (
            'last_login','date_joined')

class ClientProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClientProfile
		fields = ('id',)

class HostProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = HostProfile
		fields = ('id',)