from django.shortcuts import render, get_object_or_404
from .models import Hospital
from accounts.models import User
from reviews.models import HosReview
# Create your views here.
def hosProf(request, hospital_id):
    hospital =get_object_or_404(Hospital, pk= hospital_id)
    hospitalReviews = HosReview.objects.all()
    hospital_reviews = []
    for hospitalReview in hospitalReviews:
       if hospitalReview.hospital.id == hospital_id:
           data = {
               'hospital' : hospitalReview.hospital,
               'user' : hospitalReview.user,
               'rating' : hospitalReview.rating,
               'reviews' : hospitalReview.review,
               'review_date' : hospitalReview.review_date
           }
           hospital_reviews.append(data)

        
    context = {
        'hospital' : hospital,
        'hospital_reviews' : hospital_reviews
        
    }
    return render(request, 'HospitalProfile.html', context)