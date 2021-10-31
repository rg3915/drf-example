from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from blog.filters import PostFilter
from blog.models import Author, Post
from blog.pagination import CustomBlogResultsSetPagination
from blog.serializers import AuthorSerializer, PostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ('first_name', 'last_name')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(created_by__username='regis')
    serializer_class = PostSerializer
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    # pagination_class = CustomBlogResultsSetPagination
    # filterset_fields = ('title', 'body')
    filterset_class = PostFilter

    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(created_by=user)

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     username = self.request.query_params.get('username')

    #     if username:
    #         queryset = queryset.filter(created_by__username=username)
    #     return queryset

    @action(detail=True, methods=['put'])
    def like(self, request, pk=None):
        '''
        Marca Like = True
        '''
        post_obj = self.get_object()
        post_obj.like = True
        post_obj.save()
        serializer = self.get_serializer(post_obj)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def unlike(self, request, pk=None):
        '''
        Marca Like = False
        '''
        post_obj = self.get_object()
        post_obj.like = False
        post_obj.save()
        serializer = self.get_serializer(post_obj)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_posts(self, request, pk=None):
        '''
        Retorna somente os meus posts.
        '''
        user = self.request.user
        # posts = Post.objects.filter(created_by=user)
        posts = self.get_queryset().filter(created_by=user)

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
