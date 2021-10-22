from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models import Author, Post
from blog.pagination import CustomBlogResultsSetPagination
from blog.serializers import AuthorSerializer, PostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    # pagination_class = CustomBlogResultsSetPagination
