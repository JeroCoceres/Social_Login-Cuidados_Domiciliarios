from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from Users import auxiliary_models

Account = get_user_model()

class UserProfile(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    # Opciones
    genderChoices = [
        ("Hombre", "Hombre"),
        ("Mujer", "Mujer"),
        ("Otro", "Otro")
    ]

    # Modelos
    userIsWorker = models.BooleanField(default=False)  # Prescindible
    userMembership = models.CharField(blank=True, null=True, max_length=30)  # Prescindible
    userGender = models.CharField(max_length=30, choices=genderChoices, blank=False, null=False)  # Necesario
    userBirthDate = models.DateField(blank=True, null=True)  # Necesario
    userLocation = models.CharField(blank=True, null=True, max_length=30)  # Prescindible
    userDescription = models.TextField(blank=True, null=True, max_length=500)  # Prescindible
    userProvince = models.CharField(blank=True, null=True, max_length=30)  # Prescindible
    userCity = models.CharField(blank=True, null=True, max_length=30)  # Prescindible
    userPostalCode = models.PositiveSmallIntegerField(blank=True, null=True)  # Prescindible

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_groups'
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_permissions'
    # )

class UserWorkData(models.Model):
    userID = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='work_data')
    workerID = models.BigAutoField(primary_key=True,)
    MinPayment = models.FloatField()
    isStudying = models.BooleanField(default=False)
    userProfession = models.CharField(max_length=50)

class UserSkills(models.Model):
    userID = models.ManyToManyField(UserProfile, related_name='skills')
    skillID = models.ForeignKey(auxiliary_models.skillList, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    hasExperience = models.BooleanField(default=False)
    yearsOfExperience = models.PositiveSmallIntegerField()
    isVerified = models.BooleanField(default=False)

class CertificationData(models.Model):
    skillID = models.OneToOneField(UserSkills, on_delete=models.CASCADE, related_name='certification')
    certificateID = models.BigAutoField(primary_key=True)
    institution = models.CharField(max_length=255)
    certificateDate = models.DateField(blank=False, null=False)
    file = models.FileField(upload_to='certifications/')
