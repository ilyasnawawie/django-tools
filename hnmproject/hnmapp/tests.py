from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import AdminAuthToken

class AdminAuthTokenTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        AdminAuthToken.objects.create(user_id=1, created_at='2023-01-01T00:00:00Z')

    def test_get_all_admin_auth_tokens(self):
        response = self.client.get(reverse('admin_auth_tokens-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
