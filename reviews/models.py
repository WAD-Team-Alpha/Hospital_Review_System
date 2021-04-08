from django.db import models
from doctors.models import Doctor
from accounts.models import User
# Create your models here.
class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.user