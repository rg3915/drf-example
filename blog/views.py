from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

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
