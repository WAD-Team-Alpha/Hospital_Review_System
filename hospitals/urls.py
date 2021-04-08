from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:hospital_id>', views.hosProf, name="HospitalProfile"),
]