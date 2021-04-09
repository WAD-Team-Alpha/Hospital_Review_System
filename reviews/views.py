from hospitals.models import Hospital
from django.shortcuts import render, redirect
from doctors.models import Doctor
from accounts.models import User
from .models import DocReview
from .models import HosReview
# Create your views here.


def docreview(request):
    if request.method == 'POST':
        doctor_id = request.POST['doctor_id']
        doctor_name = request.POST['doctor_name']
        username = request.POST['username']
        rating = request.POST['rating']
        review = request.POST['review']
        print(doctor_name, username, rating, review, doctor_id)
        if not request.user.is_authenticated:
            print("failed")
            #messages.error(request, "Please Signin")
            return redirect('/doctors/'+doctor_id)
        user = User.objects.all().filter(Username=request.user.username).get()
        doctor = Doctor.objects.all().filter(Username=doctor_name).get()

        reviewed = DocReview(doctor=doctor, user=user, rating=rating, review=review)
        reviewed.save()
        print("success")
        return redirect('/doctors/'+doctor_id)
def hosreview(request):
    if request.method == 'POST':
        hospital_id = request.POST['hospital_id']
        hospital_name = request.POST['hospital_name']
        username = request.POST['username']
        rating = request.POST['rating']
        review = request.POST['review']
        print(hospital_name, username, rating, review, hospital_id)
        if not request.user.is_authenticated:
            print("failed")
            #messages.error(request, "Please Signin")
            return redirect('/hospitals/'+hospital_id)
        user = User.objects.all().filter(Username=request.user.username).get()
        hospital = Hospital.objects.all().filter(Username=hospital_name).get()

        reviewed = HosReview(hospital=hospital, user=user, rating=rating, review=review)
        reviewed.save()
        print("success")
        return redirect('/hospitals/'+hospital_id)