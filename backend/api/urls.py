from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import include, path
from .views import FirstStepView, SelectCourseView

router = DefaultRouter()


router.register(r"", SelectCourseView, basename="courses")

urlpatterns = [
    path("first-step/", FirstStepView.as_view(), name="first-step"),
    path("second-step/", include(router.urls)),
    path(r"", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
]
