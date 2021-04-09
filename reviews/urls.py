from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('docreveiw', views.docreview, name="docreview"),
    path('hosreveiw', views.hosreview, name="hosreview"),
]
