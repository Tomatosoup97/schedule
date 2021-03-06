from django.shortcuts import render, get_object_or_404

from rest_condition import And, Or, Not
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from core.permissions import IsSafeMethod, IsPOST
from .serializers import UserSerializer
from .serializers import HostProfileSerializer, ClientProfileSerializer
from .models import BasicUser, HostProfile, ClientProfile

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = BasicUser.objects.all()
    permission_classes = [Or(
        IsSafeMethod,
        IsPOST,
        IsAdminUser,
    )]

class HostProfileViewSet(viewsets.ModelViewSet):
    serializer_class = HostProfileSerializer
    queryset = HostProfile.objects.all()
    permission_classes = [Or(
        IsSafeMethod,
        IsPOST,
        IsAdminUser,
    )]

class ClientProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ClientProfileSerializer
    queryset = ClientProfile.objects.all()
    permission_classes = [Or(
        IsSafeMethod,
        IsPOST,
        IsAdminUser,
    )]

class UserCurrentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user