from django.db import models
from Users.models import UserWorkData, UserProfile
from Contracts.models import Contract

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Tarjeta de Credito', 'Tarjeta de Credito'),
        ('Tarjeta de Debito', 'Tarjeta de Debito'),
        ('Transferencia Bancaria ', 'Transferencia Bancaria '),
        ('MercadoPago', 'MercadoPago')
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado'),
        ('Fallido', 'Fallido')
    ]

    paymentID = models.BigAutoField(primary_key=True)
    workerID = models.ForeignKey(UserWorkData, on_delete=models.CASCADE, related_name='payment')
    payerID = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payments_made')
    amount = models.FloatField()
    paymentDateTime = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES)
    reference = models.CharField(max_length=255,blank=True,null=True)

class WorksPaid(models.Model):
    worksPaidID = models.BigAutoField(primary_key=True)
    paymentID = models.OneToOneField(Payment, on_delete=models.CASCADE)
    contractID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    periodPaidFrom = models.DateField()
    periodPaidTo = models.DateField()
    hoursPaid = models.FloatField()

