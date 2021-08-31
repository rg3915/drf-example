from blog.views import PostViewSet
from blog.views import AuthorViewSet
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)

router.register(r'posts', PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]