from django.test import TestCase

from school.models import Classroom, Student
from school.serializers import (
    ClassroomSerializer,
    StudentRegistrationSerializer,
    StudentSerializer
)


class SerializerTest(TestCase):

    def setUp(self):
        self.student = Student(registration='1', first_name='Regis', last_name='Santos')
        self.classroom = Classroom(id=1, title='Um')
        self.classroom.students.add(self.student.id)
        self.student_serializer = StudentSerializer(instance=self.student)
        self.student_registration_serializer = StudentRegistrationSerializer(instance=self.student)
        self.classroom_serializer = ClassroomSerializer(instance=self.classroom)

    def test_student_contem_campos_esperados(self):
        data = self.student_serializer.data
        esperado = set(['id', 'registration', 'first_name', 'last_name'])
        resultado = set(data.keys())
        self.assertEqual(esperado, resultado)

    def test_student_is_created(self):
        data = {'registration': '1', 'first_name': 'Regis', 'last_name': 'Santos'}
        serializer = StudentSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        esperado = {
            'id': 1,
            'registration': '1',
            'first_name': 'Regis',
            'last_name': 'Santos'
        }
        self.assertEqual(esperado, serializer.data)

    def test_student_is_updated(self):
        data = {'registration': '2'}
        serializer = StudentSerializer(self.student, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        esperado = {
            'id': 1,
            'registration': '2',
            'first_name': 'Regis',
            'last_name': 'Santos'
        }
        self.assertEqual(esperado, serializer.data)

    def test_student_registration_contem_campos_esperados(self):
        data = self.student_registration_serializer.data
        esperado = set(['registration', 'full_name'])
        resultado = set(data.keys())
        self.assertEqual(esperado, resultado)

    def test_student_registration_retorna_formato_esperados(self):
        data = self.student_registration_serializer.data
        esperado = '0000001'
        resultado = data['registration']
        self.assertEqual(esperado, resultado)

    def test_student_full_name_retorna_formato_esperados(self):
        data = self.student_registration_serializer.data
        esperado = 'Regis Santos'
        resultado = data['full_name']
        self.assertEqual(esperado, resultado)

    def test_classroom_contem_campos_esperados(self):
        data = self.classroom_serializer.data
        esperado = set(['id', 'title', 'students'])
        resultado = set(data.keys())
        self.assertEqual(esperado, resultado)
