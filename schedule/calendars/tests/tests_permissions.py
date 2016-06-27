from mock import MagicMock

from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from calendars.permissions import IsPublic, IsPrivate
from calendars.permissions import IsMeetingClient, IsMeetingHost
from users.tests.factories import ClientFactory, HostFactory
from .factories import MeetingFactory, TagFactory

class MockedAPITestCase(APITestCase):
    """
    Common TestCase class that provides in setUp
    mocked permission arguments and meeting object
    """
    def setUp(self):
        self.request = MagicMock()
        self.view = MagicMock()
        self.client = APIClient()
        self.meeting = MeetingFactory()

class TestHostClientPermissions(MockedAPITestCase):
    """
    Test IsMeetingHost permission class
    """
    def setUp(self):
        super(TestHostClientPermissions, self).setUp()
        self.permission_host = IsMeetingHost()

    def test_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        self.assertFalse(
            self.permission_host.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_user_that_is_meeting_host(self):
        user = HostFactory()
        self.meeting.hosts.add(user)
        self.request.user = user
        self.assertTrue(
            self.permission_host.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_user_that_is_not_meeting_host(self):
        self.request.user = HostFactory()
        self.assertFalse(
            self.permission_host.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

class TestMeetingClientPermissions(MockedAPITestCase):
    """
    Test IsClientHost permission class
    """
    def setUp(self):
        super(TestMeetingClientPermissions, self).setUp()
        self.permission_client = IsMeetingClient()

    def test_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        self.assertFalse(
            self.permission_client.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_user_that_is_meeting_client(self):
        user = ClientFactory()
        self.meeting.clients.add(user)
        self.request.user = user
        self.assertTrue(
            self.permission_client.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_user_that_is_not_meeting_client(self):
        self.request.user = ClientFactory()
        self.assertFalse(
            self.permission_client.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )


class TestPrivacyPermissions(MockedAPITestCase):
    """
    Test IsPublic and IsPrivate permissions
    """
    def setUp(self):
        super(TestPrivacyPermissions, self).setUp()
        self.permission_private = IsPrivate()
        self.permission_public = IsPublic()

    def test_public_meeting(self):
        self.meeting.public = True
        self.assertTrue(
            self.permission_public.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_non_public_meeting(self):
        self.meeting.public = False
        self.assertFalse(
            self.permission_public.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_private_meeting(self):
        self.meeting.private = True
        self.assertTrue(
            self.permission_private.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )

    def test_non_private_meeting(self):
        self.meeting.private = False
        self.assertFalse(
            self.permission_private.has_object_permission(
                self.request, self.view, self.meeting,
            )
        )