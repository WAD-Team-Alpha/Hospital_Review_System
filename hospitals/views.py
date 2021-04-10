from django.shortcuts import render, get_object_or_404
from .models import Hospital
from accounts.models import User
from reviews.models import HosReview
# Create your views here.
def hosProf(request, hospital_id):
    hospital =get_object_or_404(Hospital, pk= hospital_id)
    queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)[:3]
    
    if request.method == 'POST':
        queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)
        
    context = {
        'hospital' : hospital,
        'hospital_reviews' : queryset_list
        
    }
    return render(request, 'HospitalProfile.html', context)