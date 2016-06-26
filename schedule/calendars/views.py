from django.shortcuts import render, get_object_or_404
from django.db.models import  Q

from rest_condition import And, Or, Not
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from core.permissions  import IsSafeMethod, IsChange, IsPOST, IsDELETE
from users.permissions import IsSuperUser, IsHost, IsClient
from .permissions import IsPublic, IsPrivate, IsMeetingHost, IsMeetingClient
from .serializers import MeetingSerializer, CategorySerializer, TagSerializer
from .models import Meeting, Category, Tag

class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    permission_classes = [Or(
        And(
            IsSafeMethod,
            IsPublic,
        ),
        And(
            IsSafeMethod,
            Not(IsPrivate),
            IsMeetingClient,
        ),
        IsMeetingHost,
        IsAdminUser,
    )]

    def get_queryset(self):
        user = self.request.user
        if IsHost:
            return Meeting.objects.filter(
                Q(hosts=user.id) | Q(public=True))
        elif IsClient:
            return Meeting.objects.filter(
                Q(private=False),
                Q(public=True) | Q(clients=user.id))
        elif IsSuperUser:
            return Meeting.objects.all()
        else:
            return Meeting.objects.filter(public=True)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [Or(
        IsSafeMethod,
        And(
            IsHost,
            IsPOST,
        ),
        IsAdminUser,
    )]

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [Or(
        IsSafeMethod,
        And(
            IsHost,
            IsPOST,
        ),
        IsAdminUser,
    )]