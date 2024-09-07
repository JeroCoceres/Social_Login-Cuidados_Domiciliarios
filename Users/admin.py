from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, UserWorkData, UserSkills, CertificationData
from Users.auxiliary_models import skillList
from django.contrib.auth.models import Group


# Resto de las clases de admin personalizadas
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('account', 'userGender', 'userBirthDate', 'userLocation', 'userCity', 'userProvince')
    search_fields = ('account__email', 'userGender', 'userCity', 'userProvince')

class UserWorkDataAdmin(admin.ModelAdmin):
    list_display = ('userID', 'workerID', 'MinPayment', 'isStudying', 'userProfession')
    search_fields = ('userID__username', 'userProfession')

class UserSkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'hasExperience', 'yearsOfExperience', 'isVerified')
    search_fields = ('description', 'userID__username')

class CertificationDataAdmin(admin.ModelAdmin):
    list_display = ('certificateID', 'institution', 'certificateDate')
    search_fields = ('institution', 'skillID__description')

class SkillListAdmin(admin.ModelAdmin):
    list_display = ('skillID', 'skillName')
    search_fields = ('skillName',)

# Registro de los modelos con las clases de administración personalizadas
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserWorkData, UserWorkDataAdmin)
admin.site.register(UserSkills, UserSkillsAdmin)
admin.site.register(CertificationData, CertificationDataAdmin)
admin.site.register(skillList, SkillListAdmin)





