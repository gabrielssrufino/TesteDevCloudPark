from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import  models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    model = models.User
    list_display = ('email', 'username', 'is_staff', 'is_active', 'is_superuser')