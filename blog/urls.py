from django.urls import include, path
from rest_framework import routers

from blog.views import AuthorViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
