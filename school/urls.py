from django.urls import include, path
from rest_framework import routers

from school.views import ClassroomViewSet, StudentViewSet

router = routers.DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'classrooms', ClassroomViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
