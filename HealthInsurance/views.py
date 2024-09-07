from rest_framework import viewsets
from .models import HealthInsurance, HealthInsuranceLocation
from .serializers import HealthInsuranceSerializer, HealthInsuranceLocationSerializer

class HealthInsuranceViewSet(viewsets.ModelViewSet):
    queryset = HealthInsurance.objects.all()
    serializer_class = HealthInsuranceSerializer

class HealthInsuranceLocationViewSet(viewsets.ModelViewSet):
    queryset = HealthInsuranceLocation.objects.all()
    serializer_class = HealthInsuranceLocationSerializer
