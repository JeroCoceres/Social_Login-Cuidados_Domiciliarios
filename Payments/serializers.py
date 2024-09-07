from rest_framework import serializers
from .models import Payment, WorksPaid

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class WorksPaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksPaid
        fields = '__all__'
