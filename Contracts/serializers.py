from rest_framework import serializers
from .models import Contract, SkillRequired, ComfortOffered, Checklist

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class SkillRequiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillRequired
        fields = '__all__'

class ComfortOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComfortOffered
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'
