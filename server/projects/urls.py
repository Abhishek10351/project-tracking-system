from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"employees", EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
