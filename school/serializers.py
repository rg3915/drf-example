from rest_framework import serializers

from school.models import Classroom, Grade, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class StudentRegistrationSerializer(serializers.BaseSerializer):

    class Meta:
        model = Student

    def to_representation(self, instance):
        return {
            'registration': instance.registration.zfill(7),
            'full_name': instance.__str__()
        }


class ClassroomSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True)
    students = serializers.ListSerializer(child=StudentSerializer(), required=False)

    class Meta:
        model = Classroom
        fields = '__all__'
        # depth = 1


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = '__all__'
