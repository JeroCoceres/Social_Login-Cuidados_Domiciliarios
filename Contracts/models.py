from django.db import models
from Users.models import UserProfile, UserWorkData
from Patients.models import Patient
from Users.auxiliary_models import skillList

class Contract(models.Model):
    contractID = models.BigAutoField(primary_key=True)
    userMakerID = models.ManyToManyField(UserProfile, related_name='made_contracts')
    userReceiverID = models.ManyToManyField(UserWorkData, related_name='received_contracts')
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    contractStartTime = models.DateTimeField()
    contractEndTime = models.DateTimeField()
    contractStatus = models.CharField(max_length=50)
    contractDescription = models.TextField()
    maxPaymentProposed = models.FloatField()
    taskList = models.BooleanField(default=False)
    profesionalRequired = models.CharField(max_length=50)
    skillRequired = models.ManyToManyField(skillList)
    specialRequirement = models.TextField()
    contractLocation = models.CharField(max_length=255)
    paymentAgreed = models.BooleanField(default=False)

class SkillRequired(models.Model):
    skillRequiredID = models.BigAutoField(primary_key=True)
    contractID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    skillID = models.ManyToManyField(skillList)

class ComfortOffered(models.Model):
    comfortID = models.BigAutoField(primary_key=True)
    contractID = models.ManyToManyField(Contract, related_name='comforts_offered')
    comfortName = models.CharField(max_length=255)

class Checklist(models.Model):
    checklistID = models.BigAutoField(primary_key=True)
    contractID = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='checklists')
    workerID = models.ForeignKey(UserWorkData, on_delete=models.CASCADE, related_name='checklists')
    task = models.CharField(max_length=255)
    taskDescription = models.TextField()
    taskDateTime = models.DateTimeField()
    done = models.BooleanField(default=False)
    doneDateTime = models.DateTimeField(null=True, blank=True)


