from tkinter.font import names

from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.models import Course
from materials.views import (ClassCreateApiView, ClassDestroyApiView,
                             ClassListApiView, ClassRetrieveApiView,
                             ClassUpdateApiView, CourseViewSet)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("classes/", ClassListApiView.as_view(), name="classes_list"),
    path("classes/<int:pk>", ClassRetrieveApiView.as_view(), name="classes_retrieve"),
    path("classes/create/", ClassCreateApiView.as_view(), name="classes_create"),
    path("classes/<int:pk>/delete/", ClassDestroyApiView.as_view(), name="classes_delete"),
    path("classes/<int:pk>/update/", ClassUpdateApiView.as_view(), name="classes_update")
]

urlpatterns += router.urls