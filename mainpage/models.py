from django.db import models
from accounts.models import User
from doctors.models import Doctor

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    dateOfAppointment = models.DateField()
    AdditionalMessage = models.TextField(max_length=500)
    def __str__(self):
        return self.user.Username