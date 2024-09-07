from django.contrib import admin
from .models import Patient, PatientCurrentDiseases, PatientCurrentTreatments, BarthelScale

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patientID', 'patientName', 'patientSurname', 'patientGender', 'patientBirthDate')
    search_fields = ('patientName', 'patientSurname', 'patientGender')
    list_filter = ('patientGender', 'patientBirthDate')

@admin.register(PatientCurrentDiseases)
class PatientCurrentDiseasesAdmin(admin.ModelAdmin):
    list_display = ('patientID', 'diseaseName')
    search_fields = ('diseaseName',)

@admin.register(PatientCurrentTreatments)
class PatientCurrentTreatmentsAdmin(admin.ModelAdmin):
    list_display = ('patientID', 'treatmentsName')
    search_fields = ('treatmentsName',)

@admin.register(BarthelScale)
class BarthelScaleAdmin(admin.ModelAdmin):
    list_display = ('patientID', 'patientBarthelActivity', 'patientBarthelPoint')
    search_fields = ('patientBarthelActivity',)


