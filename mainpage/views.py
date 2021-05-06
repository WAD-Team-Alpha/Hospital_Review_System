from django.shortcuts import redirect, render
from accounts.models import User
from doctors.models import Doctor
from hospitals.models import Hospital
from django.contrib import messages
from .models import Appointment
from django.core.mail import send_mail


# Create your views here.

def index(request):
    '''
    in this index function we have accessed the user information if user had logged in and 
    filtered him from the database using his username from Auth.
    Here we returned details of user from database and also kind of user 
    '''
    username = request.user.username
    
    #storing all data in variables
    users = User.objects.all()
    doctors = Doctor.objects.all()
    hospitals = Hospital.objects.all()
    user_list = []
    doctor_list = []
    hospital_list = []

    for user in users:
        user_list.append(user.Username)

    for doctor in doctors:
        doctor_list.append(doctor.Username)

    for hospital in hospitals:
        hospital_list.append(hospital.Username)
    USER = None #logged in user object
    type = "default" # type of user

    # filtering the user from database
    if username in user_list:
        USER = User.objects.all().filter(Username=username).get()
        type = "user"
    elif username in doctor_list:
        USER = Doctor.objects.all().filter(Username=username).get()
        type = "doctor"
    elif username in hospital_list:
        USER = Hospital.objects.all().filter(Username=username).get()
        type = "hospital"
    
    # storing obtained values in the contexts
    context = {
        'type' : type,
        'USER' : USER
    }
    # sending context to index.html
    return render(request, 'index.html', context)


def MakeAnAppointment(request):
    # Accessing all the required info for validation
    if request.method == "POST":
        DoctorUsername = request.POST["dname"] # accessing the doctors username
        DateOfAppointment = request.POST["date"] # accessing the date of appointment
        additionalMessage = request.POST["message"] # Some additional message is accessed here

        # Checking whether the user is signed in or not
        if not request.user.is_authenticated:
            messages.error(request, "Please Signin")
            return redirect('index')        

        # retrieving the user and doctor
        user = User.objects.all().filter(Username=request.user.username).get()
        doctor = Doctor.objects.all().filter(Username=DoctorUsername).get()

        # checking whether the doctor exists or not
        if not doctor:
            messages.error(request, "Doctor Does not exists")
            return redirect('index')
        
        # saving the appointment in the database
        appointment = Appointment(user=user, doctor=doctor, dateOfAppointment=DateOfAppointment, AdditionalMessage=additionalMessage)
        appointment.save()

        # sending the email message of the appointment to both user and the doctor
        userSubject = "Reference for your appointment"
        userBody = ("Hi " + user.FirstName + user.LastName + 
                    "\n\nHere is what we got from you" + 
                    "\n\nDoctor Name: " + doctor.FirstName + doctor.LastName + 
                    "\n\nAppointment Date: " + DateOfAppointment + 
                    "\n\nAdditional Message: " + additionalMessage + 
                    "\n\nThe doctor will message to your appointment enquiry to your email in a span of 2-3 days" + 
                    "\n\nFor any queries please reply to this mail"
                )
        userEmail = request.user.email

        userEmail = send_mail (
                userSubject,
                userBody,
                "jeevannakshawad@gmail.com",
                [userEmail],
                fail_silently=False
        )

        doctorSubject = "Appointment enquiry from " + user.FirstName + user.LastName
        doctorBody = ("Hi Doctor " + doctor.FirstName + doctor.LastName + 
                    "\n\nThis is to inform you that we got an appointment request from " + user.FirstName + user.LastName + 
                    "\n\nAppointment Date: " + DateOfAppointment + 
                    "\n\nAdditional Message: " + additionalMessage + 
                    "\n\nPlease respond to his enquiry within 2-3 days, and contact with the user if necessary" + 
                    "\n\nFor any queries please reply to this mail"
                )

        doctoremail = doctor.Email

        doctorEmail = send_mail (
                doctorSubject,
                doctorBody,
                "jeevannakshawad@gmail.com",
                [doctoremail],
                fail_silently=False
        )

        messages.success(request, "Appointment Sent!! Wait for the doctor to reply") # success message
        return redirect('index')

