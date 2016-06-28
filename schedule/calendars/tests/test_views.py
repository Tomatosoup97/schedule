from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from users.tests.factories import ClientFactory, HostFactory
from .factories import MeetingFactory, TagFactory, CategoryFactory

class CategoryViewSetTest(APITestCase):

    # GET Methods
    
    def test_category_detail_get(self):
        category = CategoryFactory()
        url = reverse('calendar:category-detail', kwargs={'pk': category.id })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_list_get(self):
        url = reverse('calendar:category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # POST Methods

    def test_category_creation_as_unauthenticated(self):
        url = reverse('calendar:category-list')
        data = { 'name': 'category_name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_creation_as_client(self):
        client_user = ClientFactory()
        self.client.login(
            username=client_user.user.username,
            password=client_user.user.password,)
        url = reverse('calendar:category-list')
        data = { 'name': 'category_name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_category_creation_as_host(self):
        host_user = HostFactory()
        self.client.login(
            username=host_user.user.username,
            password=host_user.user.password,)
        url = reverse('calendar:category-list')
        data = { 'name': 'category_name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)        

class TagViewSetTest(APITestCase):

    # GET Methods
    
    def test_tag_detail_get(self):
        tag = TagFactory()
        url = reverse('calendar:tag-detail', kwargs={'pk': tag.id })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_list_get(self):
        url = reverse('calendar:tag-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_creation_as_unauthenticated(self):
        url = reverse('calendar:tag-list')
        data = { 'name': 'tag_name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # POST Methods

    def test_tag_creation_as_client(self):
        client_user = ClientFactory()
        self.client.login(
            username=client_user.user.username,
            password=client_user.user.password,)
        url = reverse('calendar:tag-list')
        data = { 'name': 'tag_name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_tag_creation_as_host(self):
        host_user = HostFactory()
        self.client.login(
            username=host_user.user.username,
            password=host_user.user.password,)
        url = reverse('calendar:tag-list')
        data = { 'name': 'tag_name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)