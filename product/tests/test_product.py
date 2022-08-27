import json

from autenticacao.token import TokenSerializer
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from product.models import Product


class BaseSetup(TestCase):

    def setUp(self):

        self.loja = {"title": "Produto Um"}

    def test_create_product(self):
        self.user = get_user_model().objects.create_user('admin', 'd')
        # self.client.force_login(self.user)
        response = self.client.post(
            '/api/v1/auth/jwt/create/',
            data={'username': 'admin', 'password': 'd'},
            content='application/json'
        )
        print(response.content)
