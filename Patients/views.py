from rest_framework import viewsets
from .models import Patient, PatientCurrentDiseases, PatientCurrentTreatments, BarthelScale
from .serializers import PatientSerializer, PatientCurrentDiseasesSerializer, PatientCurrentTreatmentsSerializer, BarthelScaleSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientCurrentDiseasesViewSet(viewsets.ModelViewSet):
    queryset = PatientCurrentDiseases.objects.all()
    serializer_class = PatientCurrentDiseasesSerializer

class PatientCurrentTreatmentsViewSet(viewsets.ModelViewSet):
    queryset = PatientCurrentTreatments.objects.all()
    serializer_class = PatientCurrentTreatmentsSerializer

class BarthelScaleViewSet(viewsets.ModelViewSet):
    queryset = BarthelScale.objects.all()
    serializer_class = BarthelScaleSerializer
