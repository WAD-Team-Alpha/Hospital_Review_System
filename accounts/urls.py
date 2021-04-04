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
    path('signout', views.signout, name="Signout"),
    path('activate/<uidb64>/<token>', views.verificationView.as_view(), name="activate"),
]
