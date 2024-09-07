from django.db import models
from HealthInsurance.models import HealthInsurance

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro')
    ]

    patientID = models.BigAutoField(primary_key=True)
    patientName = models.CharField(max_length=50)
    patientSurname = models.CharField(max_length=50)
    patientGender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    patientBirthDate = models.DateField()
    patientDescription = models.TextField(blank=True, null=True)
    patientFIMScale = models.PositiveSmallIntegerField()
    healthInsuranceID = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE)
    healthInsuranceMemberID = models.PositiveIntegerField()

class PatientCurrentDiseases(models.Model):
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diseaseName = models.CharField(max_length=100)

class PatientCurrentTreatments(models.Model):
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatmentsName = models.CharField(max_length=100)

class BarthelScale(models.Model):
    patientID = models.OneToOneField(Patient, on_delete=models.CASCADE)
    patientBarthelActivity = models.CharField(max_length=100)
    patientBarthelPoint = models.PositiveSmallIntegerField()

