import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from school.models import Student
from school.serializers import StudentSerializer


class ViewSetTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='d')
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.student = Student.objects.create(
            registration='1',
            first_name='Regis',
            last_name='Santos'
        )
        self.student_serializer = StudentSerializer(instance=self.student)

    def test_student_list(self):
        response = self.client.get(
            '/school/students/',
            content_type='application/json',
        )
        resultado = json.loads(response.content)
        esperado = [
            {
                "id": 1,
                "registration": "1",
                "first_name": "Regis",
                "last_name": "Santos"
            }
        ]
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_create(self):
        payload = {
            "registration": "1",
            "first_name": "Regis",
            "last_name": "Santos"
        }
        response = self.client.post(
            '/school/students/',
            data=payload,
            content_type='application/json'
        )
        esperado = {
            "id": 1,
            "registration": "1",
            "first_name": "Regis",
            "last_name": "Santos"
        }
        resultado = json.loads(response.content)
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_students(self):
        response = self.client.get(
            '/school/students/all_students/',
            content_type='application/json',
        )
        resultado = json.loads(response.content)
        esperado = [
            {
                "registration": "0000001",
                "full_name": "Regis Santos"
            }
        ]
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
