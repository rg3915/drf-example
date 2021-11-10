from django.urls import include, path
from rest_framework import routers

from movie.views import CategoryViewSet, MovieViewSet

router = routers.DefaultRouter()

# router.register(prefix, viewset)
router.register(r'movies', MovieViewSet, basename="movie")
router.register(r'categories', CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
