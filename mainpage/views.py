from django.shortcuts import redirect, render
from accounts.models import User
from doctors.models import Doctor
from hospitals.models import Hospital
from django.contrib import messages
from .models import Appointment
from django.core.mail import send_mail


# Create your views here.
def index(request):
     
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
    #this is used for just for development purpose in future it might be removed
    id = 2
    context = {
        'users' : user_list,
        'doctors' : doctor_list,
        'hospitals' : hospital_list,
        'id' : id
    }

    return render(request, 'index.html', context)


def MakeAnAppointment(request):
    if request.method == "POST":
        DoctorUsername = request.POST["dname"]
        DateOfAppointment = request.POST["date"]
        additionalMessage = request.POST["message"]

        if not request.user.is_authenticated:
            messages.error(request, "Please Signin")
            return redirect('index')        

        user = User.objects.all().filter(Username=request.user.username).get()
        print(user)
        doctor = Doctor.objects.all().filter(Username=DoctorUsername).get()
        print(doctor)

        if not doctor:
            messages.error(request, "Doctor Does not exists")
            return redirect('index')
        
        appointment = Appointment(user=user, doctor=doctor, dateOfAppointment=DateOfAppointment, AdditionalMessage=additionalMessage)

        appointment.save()

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

        messages.success(request, "Appointment Sent!! Wait for the doctor to reply")
        return redirect('index')

