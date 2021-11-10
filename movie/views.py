from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from movie.models import Category, Movie
from movie.serializers import CategorySerializer, MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    # queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.filter(title__icontains='lorem')

    @action(detail=False, methods=['get'])
    def get_good_movies(self, request, pk=None):
        '''
        Retorna somente filmes bons, com rating maior ou igual a 4.
        '''
        movies = Movie.objects.filter(rating__gte=4)

        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
