from django.urls import include, path
from rest_framework import routers

from school.views import ClassroomViewSet
from school.viewsets import StudentViewSet as SimpleStudentViewSet

router = routers.DefaultRouter()

router.register(r'students', SimpleStudentViewSet, basename='student')
router.register(r'classrooms', ClassroomViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
