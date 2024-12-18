from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, EmployeeViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]