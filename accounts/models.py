
from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_developer = models.BooleanField(default=False)
  is_recruiter = models.BooleanField(default=False)
  allow_notification=models.BooleanField(default=False)

  def __str__(self):
      return self.username

