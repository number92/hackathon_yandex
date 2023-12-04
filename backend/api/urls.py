from rest_framework.routers import DefaultRouter

from django.urls import include, path

from backend.api.views import CourseViewSet

router = DefaultRouter()


router.register('first-page', CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]