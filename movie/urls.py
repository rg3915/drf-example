from django.urls import include, path
from rest_framework import routers

from movie.views import CategoryViewSet, MovieViewSet

router = routers.SimpleRouter()

# router.register(prefix, viewset)
router.register(r'movies', MovieViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
