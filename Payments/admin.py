from django.contrib import admin
from .models import Payment, WorksPaid

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('paymentID', 'workerID', 'payerID', 'amount', 'paymentDateTime', 'paymentMethod', 'status', 'reference')


@admin.register(WorksPaid)
class WorksPaidAdmin(admin.ModelAdmin):
    list_display = ('worksPaidID', 'paymentID', 'contractID', 'periodPaidFrom', 'periodPaidTo', 'hoursPaid')
