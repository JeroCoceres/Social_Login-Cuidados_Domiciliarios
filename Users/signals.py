from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Crear el perfil automáticamente
        UserProfile.objects.create(account=instance)

        # Asignar el grupo "Normal_User" automáticamente
        normal_user_group, created = Group.objects.get_or_create(name='Normal_User')
        instance.groups.add(normal_user_group)

        # Asignar permisos específicos automáticamente
        # Aquí puedes agregar cualquier permiso que desees asignar al usuario recién creado
        permissions = Permission.objects.filter(
            codename__in=[
                'add_checklist',
                'change_checklist',
                'delete_checklist',
                'view_checklist',
                # Agrega otros permisos que quieras asignar aquí
            ]
        )
        instance.user_permissions.set(permissions)

        # Guardar cambios en el usuario
        instance.save()
