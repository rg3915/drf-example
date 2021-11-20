import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from school.models import Classroom, Student
from school.serializers import ClassroomSerializer, StudentSerializer


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
            # content_type='application/json',
            format='json'
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
            # content_type='application/json'
            format='json'
        )
        esperado = {
            "id": 2,
            "registration": "1",
            "first_name": "Regis",
            "last_name": "Santos"
        }
        resultado = json.loads(response.content)
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_retrieve(self):
        response = self.client.get(
            '/school/students/1/',
            format='json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "id": 1,
            "registration": "1",
            "first_name": "Regis",
            "last_name": "Santos"
        }
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_partial_update(self):
        payload = {"registration": "2"}
        response = self.client.patch(
            '/school/students/1/',
            data=payload,
            format='json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "id": 1,
            "registration": "2",
            "first_name": "Regis",
            "last_name": "Santos"
        }
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_delete(self):
        response = self.client.delete(
            '/school/students/1/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_all_students(self):
        response = self.client.get(
            '/school/students/all_students/',
            format='json'
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


class ClassroomViewSetTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='d')
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.classroom = Classroom.objects.create(title='Lorem')
        self.classroom_serializer = ClassroomSerializer(instance=self.classroom)

    def test_classroom_list(self):
        response = self.client.get(
            '/school/classrooms/',
            format='json'
        )
        _resultado = json.loads(response.content)
        resultado = _resultado['results']
        esperado = [
            {
                "id": 1,
                "title": "Lorem",
                "students": []
            }
        ]
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_create(self):
        payload = {
            "title": "Lorem"
        }
        response = self.client.post(
            '/school/classrooms/',
            data=payload,
            format='json'
        )
        esperado = {
            "id": 2,
            "title": "Lorem",
            "students": []
        }
        resultado = json.loads(response.content)
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_retrieve(self):
        response = self.client.get(
            '/school/classrooms/1/',
            format='json'
        )
        resultado = json.loads(response.content)
        esperado = {
            "id": 1,
            "title": "Lorem",
            "students": []
        }
        self.assertEqual(esperado, resultado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
