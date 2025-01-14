from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_type_choices = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    user_type = models.CharField(max_length=10, choices=user_type_choices)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.username
