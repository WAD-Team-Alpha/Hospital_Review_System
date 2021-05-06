from django.contrib import admin
from django.urls import path
from . import views
#define all path for doctor profile and doctor_search_bar

urlpatterns = [
    path('search-results', views.searchRes, name="searchRes"),
    path('<int:doctor_id>', views.docProf, name="DoctorProfile"),
    path('updateProf', views.updateProf, name="UpdateProfile"),
]
