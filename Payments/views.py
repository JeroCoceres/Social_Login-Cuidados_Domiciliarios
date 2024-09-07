from rest_framework import viewsets
from .models import Payment, WorksPaid
from .serializers import PaymentSerializer, WorksPaidSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class WorksPaidViewSet(viewsets.ModelViewSet):
    queryset = WorksPaid.objects.all()
    serializer_class = WorksPaidSerializer
