from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search-results', views.searchRes, name="searchRes"),
    path('<int:doctor_id>', views.docProf, name="DoctorProfile"),
]
