from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('appointment', views.MakeAnAppointment, name="appointment")
]

























































































# appointment = Appointment(user=yourUserame, doctor=DoctorUsername, 
#                     yourEmail=yourEmail, dateOfAppointment=DateOfAppointment, yourPhonenumber=phoneNumber,
#                     AdditionalMessage=additionalMessage)
#         appointment.save()