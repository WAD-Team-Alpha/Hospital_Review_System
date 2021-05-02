from django.db import models
from .choices import *
# Create your models here.

class Hospital(models.Model):
    HospitalName = models.CharField(max_length=150)
    HospitalRegisterationNumber = models.CharField(max_length=150)
    HospitalLicense = models.FileField(upload_to="HospitalDocuments/")
    HospitalPhoto = models.FileField(upload_to="HospitalPhotos/", blank=True)
    Email = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    HospitalEshtablishDate = models.DateField()
    HospitalDescription = models.TextField(max_length=250, blank=True)
    Rating = models.DecimalField(max_digits=2, decimal_places = 1, default=0.0)
    Ratings_stars = models.CharField(max_length=5,default="", blank=True)
    non_stars = models.CharField(max_length=5,default="12345")
    Ratings_count = models.IntegerField(default=0)  
    Town = models.CharField(max_length=150)
    City = models.CharField(max_length=150)
    Pincode = models.CharField(max_length=150)
    State = models.IntegerField(choices=States, default=1)
    ChiefMedicalOfficer = models.CharField(max_length=150)
    ChiefMedicalOfficerCertificate = models.FileField(upload_to="ChiefDoctorDocuments/")
    ChiefMedicalOfficerPhoto = models.FileField(upload_to="ChiefDoctorPhotos/", blank=True)
    CheifMedicalOfficerDescription = models.CharField(max_length=250, blank=True)
    PhoneNumber = models.CharField(max_length=20)
    Achievements1 = models.CharField(max_length=50, blank=True)
    Achievements2 = models.CharField(max_length=50, blank=True)
    Achievements3 = models.CharField(max_length=50, blank=True)
    Achievements4 = models.CharField(max_length=50, blank=True)
    Achievements5 = models.CharField(max_length=50, blank=True)
    Achievements6 = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.HospitalName