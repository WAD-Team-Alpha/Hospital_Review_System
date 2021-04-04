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
    if request.method == "POST":
        hospform = HospitalForm(request.POST, request.FILES)
        username = request.POST['Username']
        password = request.POST['psw']
        print(username)
        if User.objects.filter(username=username).exists():
            return render(request, 'Hospitalregistion.html', {"form": hospform, "data": "Username Already Exists"})

        if hospform.is_valid():
            # Create user
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Save the Data to the Database 
            hospform.save()
            
            #automatically login the user for the firsttime
            user = auth.authenticate(request, username=username, password=password)
            print("User Created")
            if user is not None:
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'Hospitalregistion.html', {"form": hospform, "data": hospform.errors})

    else:
        hospform = HospitalForm()
    return render(request, 'Hospitalregistion.html', {"form": hospform, "data": ""})

def userReg(request):
    if request.method == "POST":
        userform = UserForm(request.POST, request.FILES)
        username = request.POST['Username']
        password = request.POST['psw']
        email=request.POST['Email']
        print(username)
        if User.objects.filter(username=username).exists():
            return render(request, 'user_registration.html', {"form": userform, "data": "Username Already Exists"})

        if User.objects.filter(email=email).exists():
            return render(request, 'user_registration.html', {"form": userform, "data": "Email Already Exists"})

        if userform.is_valid():
            # Create user
            user = User.objects.create_user(username=username, password=password)
            user.is_active = False
            user.save()
            
            # Save the Data to the Database 
            userform.save()
            
            #automatically login the user for the firsttime
            user = auth.authenticate(request, username=username, password=password)
            print("User Created")
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                return redirect('index')
        else:
            return render(request, 'user_registration.html', {"form": userform, "data": userform.errors})

    else:
        userform = UserForm()
    return render(request, 'user_registration.html', {"form": userform, "data": ""})

def forgPass(request):
    return render(request, 'forgot_password.html')

def signinFail(request):
    return render(request, 'signin_fail.html')
    
def signout(request):
    auth.logout(request)
    usertype = ""
    return redirect('index')

