from rest_framework import serializers
from .models import HealthInsurance, HealthInsuranceLocation

class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurance
        fields = '__all__'

class HealthInsuranceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsuranceLocation
        fields = '__all__'
