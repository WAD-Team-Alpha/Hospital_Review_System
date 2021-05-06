from django.contrib import admin
from django.urls import path
from . import views
#define all path for hospital profile and Hospital_search_bar
urlpatterns = [
    path('<int:hospital_id>', views.hosProf, name="HospitalProfile"),
    path('hos-search-results', views.hosSearch, name="hospsearchRes"),
    path('updateProf', views.updateProf, name="HosUpdateProfile"),
]