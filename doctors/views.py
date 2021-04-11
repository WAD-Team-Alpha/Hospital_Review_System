from django.shortcuts import render, get_object_or_404
from .models import Doctor
from accounts.models import User
from reviews.models import DocReview
# Create your views here.


def docProf(request, doctor_id):
    doctor =get_object_or_404(Doctor, pk= doctor_id)
    queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)[:3]
    flag = 0
    if request.method == 'POST':
        flag = 1
        queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)
        
    
 
    context = {
        'doctor' : doctor,
        'doctor_reviews' : queryset_list,
        'flag' : flag
    }
    return render(request, 'DoctorProfile.html', context)

def searchRes(request):
    return render(request, 'searchbarResults.html')