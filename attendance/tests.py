from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class UserPermissionTests(TestCase):
    def test_create_user_incorrect_method(self):
        response = self.client.get(reverse("new-user"), {
            "user": "thisisthenameofanewuser",
            "email": "defrealemail@example.com",
            "permission": "2"
        })
        self.assertEqual(response.status_code, 405)
    def test_create_user_unauthenticated(self):
        response = self.client.post(reverse("new-user"), {
            "user": "thisisthenameofanewuser",
            "email": "defrealemail@example.com",
            "permission": "2"
        })
        print(response.headers)
        self.assertEqual(response.status_code, 302)