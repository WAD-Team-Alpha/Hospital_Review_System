from django.db import models
from .choices import *
from PIL import Image
# Create your models here.

class Doctor(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Username = models.CharField(max_length=150, default="")
    DateOfBirth = models.CharField(max_length=150)
    ProfilePhoto = models.FileField(upload_to="DoctorPhotos/", default="DoctorPhotos/boy_avatar.jpg")
    MobileNumber = models.CharField(max_length=10)
    DoctorLicense = models.FileField(upload_to="DoctorDocuments/")
    YearsOfExperience = models.IntegerField(blank=True)
    Rating = models.DecimalField(max_digits=2, decimal_places = 1, default=0.0) 
    Ratings_stars = models.CharField(max_length=5,default="", blank= True)
    non_stars = models.CharField(max_length=5,default="12345")
    Ratings_count = models.IntegerField(default=0) 
    Education = models.CharField(max_length=250, blank=True)
    Masters = models.CharField(max_length=250, blank=True)
    HospitalName = models.CharField(max_length=50)
    HospitalRegisterationNumber = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.IntegerField(choices=States, default=1)
    Pincode = models.CharField(max_length=20)
    Department = models.IntegerField(choices=Department, default=1)
    Description = models.CharField(max_length=150, default="Dear, be strong because your life will be better now. Time does not remain same. You will get well soon!")
    Achievements1 = models.CharField(max_length=50, default="No achievements added recently")
    Achievements2 = models.CharField(max_length=50, default="No achievements added recently")
    Achievements3 = models.CharField(max_length=50, default="No achievements added recently")
    Achievements4 = models.CharField(max_length=50, default="No achievements added recently")
    def __str__(self):
        return self.Username
    
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.ProfilePhoto.path) # Open image using self

        if img.height > 350 or img.width > 350:
            new_img = (350, 350)
            img.thumbnail(new_img)
            img.save(self.ProfilePhoto.path)
    
    def get_image(self):
        if self.ProfilePhoto and hasattr(self.ProfilePhoto, 'url'):
            return self.ProfilePhoto
        else:
            return "#"