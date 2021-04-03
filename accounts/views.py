from django.shortcuts import render, redirect
from hospitals.forms import HospitalForm
from doctors.forms import DoctorForm
from .forms import UserForm
from django.views import View
from django.contrib import auth
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django import forms

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print(username, password)
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return redirect('index')
        else:
           
            return render(request, 'signin_fail.html')

        
    else:
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
def signout(request):
    auth.logout(request)
    usertype = ""
    return redirect('index')

