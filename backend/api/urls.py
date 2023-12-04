from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import FirstStepView

router = DefaultRouter()


router.register(r"first-step", FirstStepView, basename="first-step")


urlpatterns = [
    path("", include(router.urls)),
]
