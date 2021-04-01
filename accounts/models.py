from django.db import models
from .choices import *

# Create your models here.

class Users(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    DateOfBirth = models.CharField(max_length=150)
    MobileNumber = models.CharField(max_length=10)

class Doctors(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    DateOfBirth = models.CharField(max_length=150)
    MobileNumber = models.CharField(max_length=10)
    DoctorLicense = models.FileField(upload_to="DoctorDocuments/")
    YearsOfExperience = models.IntegerField()
    Education = models.CharField(max_length=250)
    Masters = models.CharField(max_length=250)
    HospitalName = models.CharField(max_length=50)
    Department = models.IntegerField(choices=Department, default=1)
    Description = models.CharField(max_length=150)
    Achievements1 = models.CharField(max_length=50)
    Achievements2 = models.CharField(max_length=50)
    Achievements3 = models.CharField(max_length=50)
    Achievements4 = models.CharField(max_length=50)