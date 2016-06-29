from mock import MagicMock

from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from users import permissions
from users.models import BasicUser
from .factories import UserFactory, ClientFactory, HostFactory

class MockedAPITestCase(APITestCase):
    """
    Common TestCase class that provides in setUp
    mocked permission arguments
    """
    def setUp(self):
        self.request = MagicMock()
        self.view = MagicMock()
        self.client = APIClient()

class IsHostPermissionsTest(MockedAPITestCase):
    """
    Test IsHost permission class
    """ 
    def setUp(self):
        super(IsHostPermissionsTest, self).setUp()
        self.permission_host = permissions.IsHost()

    def test_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )
        
    def test_client_user(self):
        client_user = ClientFactory()
        user = client_user.user
        self.request.user = user
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )

    def test_host_user(self):
        host_user = HostFactory()
        user = host_user.user
        self.request.user = user
        self.assertTrue(
            self.permission_host.has_permission(self.request, self.view)
        )

class IsClientPermissionsTest(MockedAPITestCase):
    """
    Test IsClient permission class
    """ 
    def setUp(self):
        super(IsClientPermissionsTest, self).setUp()
        self.permission_host = permissions.IsClient()

    def test_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )
        
    def test_client_user(self):
        client_user = ClientFactory()
        user = client_user.user
        self.request.user = user
        self.assertTrue(
            self.permission_host.has_permission(self.request, self.view)
        )

    def test_host_user(self):
        host_user = HostFactory()
        user = host_user.user
        self.request.user = user
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )

class IsSuperUserPermissionsTest(MockedAPITestCase):
    """
    Test IsClient permission class
    """ 
    def setUp(self):
        super(IsSuperUserPermissionsTest, self).setUp()
        self.permission_host = permissions.IsSuperUser()

    def test_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )
        
    def test_client_user(self):
        client_user = ClientFactory()
        user = client_user.user
        self.request.user = user
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )

    def test_host_user(self):
        host_user = HostFactory()
        user = host_user.user
        self.request.user = user
        self.assertFalse(
            self.permission_host.has_permission(self.request, self.view)
        )

    def test_super_user(self):
        superuser = BasicUser.objects.create_superuser(
            username='username', email='tomato@soup.com', password='password')
        self.request.user = superuser
        self.assertTrue(
            self.permission_host.has_permission(self.request, self.view)
        )
