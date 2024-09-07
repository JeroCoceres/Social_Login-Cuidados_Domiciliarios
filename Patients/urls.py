from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientCurrentDiseasesViewSet, PatientCurrentTreatmentsViewSet, BarthelScaleViewSet

router = DefaultRouter()
router.register(r'list', PatientViewSet)
router.register(r'current-diseases', PatientCurrentDiseasesViewSet)
router.register(r'current-treatments', PatientCurrentTreatmentsViewSet)
router.register(r'barthel-scale', BarthelScaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
