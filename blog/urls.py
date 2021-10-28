from django.urls import include, path
from rest_framework import routers

from blog.views import AuthorViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet, basename='Author')
router.register(r'posts', PostViewSet, basename='Post')

urlpatterns = [
    path("", include(router.urls)),
]
