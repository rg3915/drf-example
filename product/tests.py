from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class Base(TestCase):

    def setUp(self):

        self.loja = {"title": "Produto Um"}

    def test_create_product(self):
        self.user = get_user_model().objects.create_user(username='admin', password='d')
        # self.client.force_login(self.user)
        response = self.client.post(
            '/api/v1/auth/jwt/create/',
            data={'username': 'admin', 'password': 'd'},
            content='application/json'
        )
        print(response.json())
