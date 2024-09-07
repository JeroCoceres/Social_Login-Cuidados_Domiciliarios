from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/auth/', include('social_accounts.urls')),

    path('contracts/', include('Contracts.urls')),
    path('users/', include('Users.urls')),
    path('patients/', include('Patients.urls')),
    path('payments/', include('Payments.urls')),
    path('healthinsurance/', include('HealthInsurance.urls')),
    path('courses/', include('Courses.urls')),
]
