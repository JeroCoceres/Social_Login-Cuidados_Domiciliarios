from django.contrib import admin
from .models import Contract, SkillRequired, ComfortOffered, Checklist

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contractID', 'contractStartTime', 'contractEndTime', 'contractStatus', 'maxPaymentProposed')
    search_fields = ('contractID', 'contractDescription', 'contractStatus')
    list_filter = ('contractStatus', 'contractStartTime', 'contractEndTime')
    filter_horizontal = ('userMakerID', 'userReceiverID', )#'skillRequired')

@admin.register(SkillRequired)
class SkillRequiredAdmin(admin.ModelAdmin):
    list_display = ('skillRequiredID', 'contractID')
    search_fields = ('skillRequiredID', 'contractID')
    #filter_horizontal = ('skillRequiredID',)

@admin.register(ComfortOffered)
class ComfortOfferedAdmin(admin.ModelAdmin):
    list_display = ('comfortID', 'comfortName')
    search_fields = ('comfortID', 'comfortName')
    filter_horizontal = ('contractID',)

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('checklistID', 'contractID', 'workerID', 'task', 'taskDateTime', 'done')
    search_fields = ('checklistID', 'contractID', 'workerID', 'task')
    list_filter = ('done', 'taskDateTime')

