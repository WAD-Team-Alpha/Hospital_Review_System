from django.shortcuts import render
from accounts.models import User
from doctors.models import Doctor
from hospitals.models import Hospital



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
    id = 1
    context = {
        'users' : user_list,
        'doctors' : doctor_list,
        'hospitals' : hospital_list,
        'id' : id
    }
    return render(request, 'index.html', context)
