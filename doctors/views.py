from django.shortcuts import render, get_object_or_404
from .models import Doctor
from accounts.models import User
from reviews.models import DocReview
# Create your views here.


def docProf(request, doctor_id):
    doctor =get_object_or_404(Doctor, pk= doctor_id)
    doctorReviews = DocReview.objects.all()
    doctor_reviews = []
    for doctorReview in doctorReviews:
       if doctorReview.doctor.id == doctor_id:
           data = {
               'doctor' : doctorReview.doctor,
               'user' : doctorReview.user,
               'rating' : doctorReview.rating,
               'reviews' : doctorReview.review,
               'review_date' : doctorReview.review_date
           }
           doctor_reviews.append(data)

        
    context = {
        'doctor' : doctor,
        'doctor_reviews' : doctor_reviews
        
    }
    return render(request, 'DoctorProfile.html', context)

def searchRes(request):
    return render(request, 'searchbarResults.html')