from collections import OrderedDict

from django.test import TestCase

from movie.models import Category, Movie
from movie.serializers import CategorySerializer, MovieSerializer


class SerializerTest(TestCase):

    def setUp(self):
        self.category = Category(title='Ficção')
        self.movie = Movie(
            title='Matrix',
            sinopse='Filme de ficção',
            rating=5,
            like=True
        )
        self.movie_serializer = MovieSerializer(instance=self.movie)
        self.category_serializer = CategorySerializer(instance=self.category)

    def test_movie_contem_campos_esperados(self):
        data = self.movie_serializer.data
        esperado = set(['id', 'title', 'sinopse', 'rating', 'like', 'category'])
        resultado = set(data.keys())
        self.assertEqual(esperado, resultado)

    def test_movie_is_created(self):
        data = {
            'title': 'Vingadores Ultimato',
            'sinopse': 'Filme de super-heróis',
            'rating': 5,
            'like': True,
            'category': {
                'title': 'Ficção'
            }
        }
        serializer = MovieSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        esperado = {
            'id': 1,
            'title': 'Vingadores Ultimato',
            'sinopse': 'Filme de super-heróis',
            'rating': 5,
            'like': True,
            'category': OrderedDict([('id', 1), ('title', 'Ficção')])
        }
        self.assertEqual(esperado, serializer.data)

    def test_movie_is_updated(self):
        data = {
            'rating': 6,
            'category': {
                'title': 'Ação'
            }
        }
        # movie = Movie.objects.get(title='Matrix')
        serializer = MovieSerializer(self.movie, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        esperado = {
            'id': 1,
            'title': 'Matrix',
            'sinopse': 'Filme de ficção',
            'rating': 6,
            'like': True,
            'category': OrderedDict([('id', 1), ('title', 'Ação')])
        }
        self.assertEqual(esperado, serializer.data)

    def test_category_contem_campos_esperados(self):
        data = self.category_serializer.data
        esperado = set(['id', 'title'])
        resultado = set(data.keys())
        self.assertEqual(esperado, resultado)

    def test_category_is_created(self):
        data = {'title': 'Ação'}
        serializer = CategorySerializer(data=data)
        serializer.is_valid()
        serializer.save()
        esperado = {
            'id': 1,
            'title': 'Ação'
        }
        self.assertEqual(esperado, serializer.data)

    def test_category_is_updated(self):
        data = {'title': 'Ficção'}
        serializer = CategorySerializer(self.category, data=data)
        serializer.is_valid()
        serializer.save()
        esperado = {
            'id': 1,
            'title': 'Ficção'
        }
        self.assertEqual(esperado, serializer.data)
