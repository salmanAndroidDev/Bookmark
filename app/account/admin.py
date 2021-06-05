from django.contrib import admin
from account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin class"""
    list_display = ('user', 'date_of_birth', 'photo')
