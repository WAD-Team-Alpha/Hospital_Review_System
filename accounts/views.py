from django.shortcuts import render, redirect
from hospitals.forms import HospitalForm
from doctors.forms import DoctorForm
from .forms import UserForm
from django.views import View
from django.contrib import auth
from django.contrib import messages, auth
from django.contrib.auth.models import User
from hospitals.models import Hospital
from django import forms
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from accounts.Utils import token_generator

# Create your views here.

def signin(request):
    '''
    this function is used to validate the user credentials and then get signed in the eligible 
    users of the web app
    '''
    # getting credentials using POST method
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # below line will validate credentials and store the returned data of the user
        user = auth.authenticate(request, username=username, password=password)
        
        # based on returned value user get logged .
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Signed in successfully")
            return redirect('index')
        else:
           
            return render(request, 'signin_fail.html')

    else:
        return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')


def hospReg(request):
    if request.method == "POST":
        # Creating an instance of the hospital registeration form for validation
        hospform = HospitalForm(request.POST, request.FILES)

        # Accessing all the required information for authentication and validation
        username = request.POST['Username']
        password = request.POST['psw']
        email = request.POST['Email']
        hospreg = request.POST['HospitalRegisterationNumber']

        # variables used for storing the error messages
        emailerror = ""
        usernameerror = ""
        regerror = ""

        # Fetching the database whether the particular hospital information is already available or not
        # Checking whether the email exists or not
        if User.objects.filter(email=email).exists():
            emailerror = "Email already exists"
        else:
            emailerror = ""

        # Checking whether the username exists or not
        if User.objects.filter(username=username).exists():
            usernameerror = "Username already exists"
        else:
            usernameerror = ""

        # Checking whether the registeration number exists or not
        if Hospital.objects.filter(HospitalRegisterationNumber=hospreg).exists():
            regerror = "A hospital is already registered with this registeration number"
        else:
            regerror = ""

        # Storing all the error messages and the hospital registeration form in a variable
        context = {
            "form": hospform,
            "regerror": regerror,
            "emailerror": emailerror,
            "usernameerror": usernameerror,
            "formerror": ""
        }

        # checking whether there exists any error message in the hospital information
        if emailerror != "" or usernameerror != "" or regerror != "":
            return render(request, 'Hospitalregistion.html', context)

        # Validating the form here
        if hospform.is_valid():
            # Create user for the hospital
            user = User.objects.create_user(username=username, password=password, email=email)
            user.is_active = False
            user.save()

            # Save the Data to the Database 
            hospform.save()

            # Sending the account activation link to his mail
            subject = "Activate Your account"
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk)) # Creating a unique uid for the hospital
            token = token_generator.make_token(user) # validating a token
            domain = get_current_site(request).domain #obtaining the current domain of the website
            link = reverse('activate', kwargs={'uidb64': uidb64, "token": token}) # combining the total link
            activate_url = 'http://'+domain+link # overall url
            body = "Hi " + username + "!\n To activate your account please click on this link\n" + activate_url # body of the mail

            # Sending the account activation link to the hospital's mail
            Email = send_mail (
                subject,
                body,
                "jeevannakshawad@gmail.com",
                [email],
                fail_silently=False
            )

            #automatically login the user for the firsttime
            user = auth.authenticate(request, username=username, password=password)
            # print("User Created")

            # Validating the hospital info
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.success(request, 'Activate your account after clicking the link sent to your mail')
                return redirect('index')
        else:
            return render(request, 'Hospitalregistion.html', {"form": hospform, "regerror": "", "emailerror": "", "usernameerror": "", "formerror": hospform.errors})

    else:
        hospform = HospitalForm()
    return render(request, 'Hospitalregistion.html', {"form": hospform, "regerror": "", "emailerror": "", "usernameerror": "", "formerror": ""})


#User Registration Function
def userReg(request):
    if request.method == "POST":
        # Creating an instance of the user registeration form for validation
        userform = UserForm(request.POST, request.FILES)
        
        # Accessing all the required information for authentication and validation
        username = request.POST['Username']
        password = request.POST['psw']
        email=request.POST['Email']

        # variables used for storing the error messages
        emailerror = ""
        usernameerror = ""

        # Fetching the database whether the particular user information is already available or not
        # Checking whether the username exists or not
        if User.objects.filter(username=username).exists():
            usernameerror = "Username already exists"
        else:
            usernameerror = ""
        
        # Checking whether the email exists or not
        if User.objects.filter(email=email).exists():
            emailerror = "Email already exists"
            
        else:
            emailerror = ""
        
        # Storing all the error messages and the user registeration form in a variable
        context = {
            "form": userform,
            "emailerror": emailerror,
            "usernameerror": usernameerror,
            "formerror": ""
        }


        # checking whether there exists any error message in the user information
        if emailerror != "" or usernameerror != "":
            return render(request, 'user_registration.html', context)

        # Validating the form here
        if userform.is_valid():
            # Create user
            user = User.objects.create_user(username=username, password=password, email=email)
            user.is_active = False
            user.save()
            
            # Save the Data to the Database 
            userform.save()

            # Sending the account activation link to his mail
            subject = "Activate Your account"
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, "token": token})
            activate_url = 'http://'+domain+link
            body = "Hi " + username + "!\n To activate your account please click on this link\n" + activate_url

             # Sending the account activation link to the user's mail
            Email = send_mail (
                subject,
                body,
                "jeevannakshawad@gmail.com",
                [email],
                fail_silently=False
            )
            
            #automatically login the user for the firsttime
            user = auth.authenticate(request, username=username, password=password)
            # print("User Created")
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.success(request, 'Activate your account after clicking the link sent to your mail')
                return redirect('index')
        else:
            return render(request, 'user_registration.html', {"form": userform,  "emailerror": "", "usernameerror": "", "formerror": userform.errors})

    else:
        userform = UserForm()
    return render(request, 'user_registration.html', {"form": userform, "emailerror": "", "usernameerror": "", "formerror": ""})


def docReg(request):
    if request.method == "POST":
        # Creating an instance of the doctor registeration form for validation
        doctorForm = DoctorForm(request.POST, request.FILES)

        # Accessing all the required information for authentication and validation
        username = request.POST['Username']
        password = request.POST['psw']
        email=request.POST['Email']

        # variables used for storing the error messages
        emailerror = ""
        usernameerror = ""

        # Fetching the database whether the particular doctor information is already available or not
        # Checking whether the username exists or not
        if User.objects.filter(username=username).exists():
            usernameerror = "Username already exists"
        else:
            usernameerror = ""

         # Checking whether the email exists or not 
        if User.objects.filter(email=email).exists():
            emailerror = "Email already exists"   
        else:
            emailerror = ""
        
        # Storing all the error messages and the doctor registeration form in a variable
        context = {
            "form": doctorForm,
            "emailerror": emailerror,
            "usernameerror": usernameerror,
            "formerror": ""
        }

        # checking whether there exists any error message in the hospital information
        if emailerror != "" or usernameerror != "":
            return render(request, 'doctor_regestration.html', context)

        # Validating the form here
        if doctorForm.is_valid():
            # Create user
            user = User.objects.create_user(username=username, password=password, email=email)
            user.is_active = False
            user.save()
            
            # Save the Data to the Database 
            doctorForm.save()
            # Sending the account activation link to his mail
            subject = "Activate Your account"
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, "token": token})
            activate_url = 'http://'+domain+link
            body = "Hi " + username + "!\n To activate your account please click on this link\n" + activate_url

            # Sending the account activation link to the doctor's mail
            Email = send_mail (
                subject,
                body,
                "jeevannakshawad@gmail.com",
                [email],
                fail_silently=False
            )
            
            #automatically login the user for the firsttime
            user = auth.authenticate(request, username=username, password=password)
            # print("User Created")
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.success(request, 'Activate your account after clicking the link sent to your mail')

                return redirect('index')
        else:
            return render(request, 'doctor_regestration.html', {"form": doctorForm,  "emailerror": "", "usernameerror": "", "formerror": doctorForm.errors})

    else:
        doctorForm = DoctorForm()
    return render(request, 'doctor_regestration.html', {"form": doctorForm, "emailerror": "", "usernameerror": "", "formerror": ""})

def forgPass(request):
    return render(request, 'forgot_password.html')

def signinFail(request):
    '''
        This function will be excuted when the user credentials are wrong or something 
        went wrong during signin process.
    '''
    return render(request, 'signin_fail.html')
    
def signout(request):
    '''
    This function will helps the user to get logged out of the website,
    this function will run only when the user presses logout button.
    '''
    auth.logout(request)
    messages.success(request, "Signed out successfully")
    return redirect('index')

# This class is used to create the activation link
class verificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            # using the token generator to generate a unique link for the particular user
            if not token_generator.check_token(user, token):
                return redirect('index'+'?message'+'User already activated')

            # If user clicks on the link sucessfully then the account will be activated
            if user.is_active:
                messages.success(request, 'Account is already active')
                return redirect('index')
            user.is_active = True
            user.save()
            auth.login(request, user) # he will be logged in for the first time sucessfully
            messages.success(request, 'Account activated successfully') # a sucess message
            return redirect('index')
        except Exception as ex:
            pass
        return redirect('index')