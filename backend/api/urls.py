from rest_framework.routers import DefaultRouter

from django.urls import include, path
from .views import FirstStepView

router = DefaultRouter()


# router.register(r"first-step", firststep_view, basename="first-step")

urlpatterns = [
    # path("", include(router.urls)),
    path("first-step/", FirstStepView.as_view(), name="first-step"),
    path(r"", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),
]
