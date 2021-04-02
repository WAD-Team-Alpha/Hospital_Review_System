from django.db import models
from .choices import *

# Create your models here.

class Doctor(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Username = models.CharField(max_length=150, default="")
    DateOfBirth = models.CharField(max_length=150)
    ProfilePhoto = models.FileField(upload_to="DoctorPhotos/", blank=True)
    MobileNumber = models.CharField(max_length=10)
    DoctorLicense = models.FileField(upload_to="DoctorDocuments/")
    YearsOfExperience = models.IntegerField(blank=True)
    Education = models.CharField(max_length=250, blank=True)
    Masters = models.CharField(max_length=250, blank=True)
    HospitalName = models.CharField(max_length=50)
    City = models.CharField(max_length=100)
    State = models.IntegerField(choices=States, default=1)
    Pincode = models.CharField(max_length=20)
    Department = models.IntegerField(choices=Department, default=1)
    Description = models.CharField(max_length=150, blank=True)
    Achievements1 = models.CharField(max_length=50, blank=True)
    Achievements2 = models.CharField(max_length=50, blank=True)
    Achievements3 = models.CharField(max_length=50, blank=True)
    Achievements4 = models.CharField(max_length=50, blank=True)