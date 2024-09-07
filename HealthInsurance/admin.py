from django.contrib import admin
from .models import HealthInsurance, HealthInsuranceLocation

@admin.register(HealthInsurance)
class HealthInsuranceAdmin(admin.ModelAdmin):
    list_display = ('healthInsuranceID', 'healthInsuranceName', 'inscriptionNumber')
    search_fields = ('healthInsuranceName', 'inscriptionNumber')

@admin.register(HealthInsuranceLocation)
class HealthInsuranceLocationAdmin(admin.ModelAdmin):
    list_display = ('healthInsuranceID', 'healthInsuranceProvinces')
    search_fields = ('healthInsuranceID__healthInsuranceName', 'healthInsuranceProvinces')
