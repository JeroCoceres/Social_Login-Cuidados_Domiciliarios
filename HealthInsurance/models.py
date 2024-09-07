from django.db import models

class HealthInsurance(models.Model):
    healthInsuranceID = models.BigAutoField(primary_key=True)
    healthInsuranceName = models.CharField(max_length=255)
    inscriptionNumber = models.IntegerField()

class HealthInsuranceLocation(models.Model):
    healthInsuranceID = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE, related_name='locations')
    healthInsuranceProvinces = models.CharField(max_length=255)
