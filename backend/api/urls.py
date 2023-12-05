from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import firststep_view, secondstep_view

router = DefaultRouter()


# router.register(r"first-step", firststep_view, basename="first-step")

urlpatterns = [
    # path("", include(router.urls)),
    path("first-step/", firststep_view, name="first-step"),
    path("second-step/", secondstep_view, name="second-step")
]
