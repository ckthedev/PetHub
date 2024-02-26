from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        blank=True,
        help_text='Specific permissions for this user.'
    )
