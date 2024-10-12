from rest_framework.serializers import ModelSerializer

from materials.models import Class, Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"