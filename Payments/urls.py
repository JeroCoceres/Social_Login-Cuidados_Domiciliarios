from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, WorksPaidViewSet

router = DefaultRouter()
router.register(r'list', PaymentViewSet)
router.register(r'works-paid', WorksPaidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
