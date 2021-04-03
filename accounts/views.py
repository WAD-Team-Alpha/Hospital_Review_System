from django.shortcuts import render
from hospitals.forms import HospitalForm
from doctors.forms import DoctorForm
from .forms import UserForm
from django.views import View
# Create your views here.

def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
def docReg(request):
    docform = DoctorForm(request.POST, request.FILES)
    return render(request, 'doctor_regestration.html', {"form": docform})
def hospReg(request):
    hospform = HospitalForm(request.POST, request.FILES)
    return render(request, 'Hospitalregistion.html', {"form": hospform})
def userReg(request):
    userform = UserForm(request.POST)
    return render(request, 'user_registration.html', {"form": userform})
def forgPass(request):
    return render(request, 'forgot_password.html')
def signinFail(request):
    return render(request, 'signin_fail.html')

