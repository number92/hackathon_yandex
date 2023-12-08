from rest_framework.routers import DefaultRouter

from django.urls import include, path
from .views import FirstStepView, SelectCourseView

router = DefaultRouter()


router.register(r"", SelectCourseView, basename="courses")

urlpatterns = [
    path("first-step/", FirstStepView.as_view(), name="first-step"),
    path("third-step/", include(router.urls)),
    path(r"", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),
]
