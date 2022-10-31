from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
   auth_key = models.CharField(max_length=500, blank=True, null=True)

   def __str__(self):
      return self.username
