from rest_framework import serializers

from school.models import Classroom, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(many=True)
    # student = serializers.ListSerializer(child=StudentSerializer())

    class Meta:
        model = Classroom
        fields = '__all__'
        depth = 1
