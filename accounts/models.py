from django.db import models
from .choices import *

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    DateOfBirth = models.CharField(max_length=150)
    MobileNumber = models.CharField(max_length=10)
    def __str__(self):
        return self.Username