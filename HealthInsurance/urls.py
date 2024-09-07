from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthInsuranceViewSet, HealthInsuranceLocationViewSet

router = DefaultRouter()
router.register(r'health-insurance', HealthInsuranceViewSet)
router.register(r'health-insurance-locations', HealthInsuranceLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
