from django.shortcuts import render
from .forms import *
from django.views import View
# Create your views here.

def signin(request):
    return render(request, 'signin.html')
def signup(request):
    return render(request, 'signup.html')
def docReg(request):
    return render(request, 'doctor_regestration.html')
def hospReg(request):
    return render(request, 'Hospitalregistion.html')
def userReg(request):
    userform = UserForm(request.POST)
    return render(request, 'user_registration.html', {"form": userform})
def forgPass(request):
    return render(request, 'forgot_password.html')
def signinFail(request):
    return render(request, 'signin_fail.html')

class Myview(View):
    def get(self, request):
        docform = DoctorForm(request.POST)
        return render(request, 'docregform.html', {"form": docform})

class hospRegForm(View):
    def get(self, request):

        return render(request, 'hospital_reg.html')

