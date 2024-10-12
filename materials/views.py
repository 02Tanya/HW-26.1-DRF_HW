from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from materials.models import Class, Course
from materials.serializers import ClassSerializer, CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ClassCreateApiView(CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassListApiView(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassRetrieveApiView(RetrieveAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUpdateApiView(UpdateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDestroyApiView(DestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer