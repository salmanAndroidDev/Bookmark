from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Profile(models.Model):
    """Custom profile model which has OneToOne relationship with User"""
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f"Profile for {self.user}"
