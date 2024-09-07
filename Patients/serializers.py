from rest_framework import serializers
from .models import Patient, PatientCurrentDiseases, PatientCurrentTreatments, BarthelScale

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientCurrentDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCurrentDiseases
        fields = '__all__'

class PatientCurrentTreatmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCurrentTreatments
        fields = '__all__'

class BarthelScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarthelScale
        fields = '__all__'
