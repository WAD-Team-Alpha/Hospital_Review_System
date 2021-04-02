from django.db import models
from .choices import *

# Create your models here.

class Users(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    DateOfBirth = models.CharField(max_length=150)
    MobileNumber = models.CharField(max_length=10)