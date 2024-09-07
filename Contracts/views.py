from rest_framework import viewsets
from .models import Contract, SkillRequired, ComfortOffered, Checklist
from .serializers import ContractSerializer, SkillRequiredSerializer, ComfortOfferedSerializer, ChecklistSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class SkillRequiredViewSet(viewsets.ModelViewSet):
    queryset = SkillRequired.objects.all()
    serializer_class = SkillRequiredSerializer

class ComfortOfferedViewSet(viewsets.ModelViewSet):
    queryset = ComfortOffered.objects.all()
    serializer_class = ComfortOfferedSerializer

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
