from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('userReg', views.userReg, name="UserRegisteration"),
    path('docReg', views.docReg, name="DoctorRegisteration"),
    path('hospReg', views.hospReg, name="HospitalRegisteration"),
    path('forgPass', views.forgPass, name="ForgotPassword"), 
    path('docRegForm', views.Myview.as_view(), name="DoctorRegistrationForm"),
    path('hospitalRegForm', views.hospRegForm.as_view(), name="HospitalRegistrationForm")

]
