from django.contrib import admin

from school.models import Classroom, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    exclude = ()
