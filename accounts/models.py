from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
       phone_number = models.CharField(max_length=15, blank=True, null=True)
       ROLES = (
           ('admin', 'Admin'),
           ('user', 'User'),
       )
       role = models.CharField(max_length=10, choices=ROLES, default='user')

       def __str__(self):
           return self.username