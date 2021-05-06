from django.db import models
from .choices import *
#  Create models forms for Hospital  details .

class Hospital(models.Model):
    HospitalName = models.CharField(max_length=150)   # Hospital Name  
    HospitalRegisterationNumber = models.CharField(max_length=150)  # Hospital Registeration 
    HospitalLicense = models.FileField(upload_to="HospitalDocuments/")
    HospitalPhoto = models.FileField(upload_to="HospitalPhotos/", default="DefaultPhotos/hospitalPhotos.jpg") #hospital photo
    Email = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    HospitalEshtablishDate = models.DateField()     # Eshtablish Date 
    HospitalDescription = models.TextField(max_length=250, default="Dear, be strong because your life will be better now. Time does not remain same. You will get well soon!")
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
    ChiefMedicalOfficerPhoto = models.FileField(upload_to="ChiefDoctorPhotos/", default="DefaultPhotos/doctt.png")
    CheifMedicalOfficerDescription = models.CharField(max_length=250, default="Dear, be strong because your life will be better now. Time does not remain same. You will get well soon!")
    PhoneNumber = models.CharField(max_length=20)
    Achievements1 = models.CharField(max_length=50, default="No Hospital information added recently")
    Achievements2 = models.CharField(max_length=50, default="No Hospital information added recently")
    Achievements3 = models.CharField(max_length=50, default="No Hospital information added recently")
    Achievements4 = models.CharField(max_length=50, default="No Hospital information added recently")
    Achievements5 = models.CharField(max_length=50, default="No Hospital information added recently")
    Achievements6 = models.CharField(max_length=50, default="No Hospital information added recently")
    def __str__(self):
        return self.HospitalName
