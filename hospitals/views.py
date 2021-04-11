from django.shortcuts import render, get_object_or_404
from .models import Hospital
from accounts.models import User
from reviews.models import HosReview
from .choices import States

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

def hosSearch(request):
    queryset_list = Hospital.objects.order_by('-HospitalName')
    State_result = States
    print(State_result)
    #dept_result = Department

    #firstname

    if 'first_name' in request.GET:
         HospitalName = request.GET['first_name']
         if HospitalName:
             queryset_list = queryset_list.filter(HospitalName__iexact = HospitalName)
          
    print(queryset_list)  
    
    #lastname
    if 'last_name' in request.GET:
        RegNo = request.GET['last_name']
        if RegNo:
            queryset_list = queryset_list.filter(HospitalRegisterationNumber__iexact = RegNo)
    print(queryset_list)  
    
    #town/village
    if 'place' in request.GET:
        Town = request.GET['place']
        if Town:
            queryset_list = queryset_list.filter(Town__iexact = Town)
    print(queryset_list)  
    #City
    if 'city' in request.GET:
        City = request.GET['city']
        if City:
            queryset_list = queryset_list.filter(City__iexact = City)
    print(queryset_list,request.GET['city'])  
    #State
    if 'state' in request.GET:
        State = request.GET['state']
        if State:
            queryset_list = queryset_list.filter(State = State)
    print(queryset_list,request.GET['state']) 
     
    #pincode
    if 'pincode' in request.GET:
         Pincode = request.GET['pincode']
         if Pincode:
             queryset_list = queryset_list.filter(Pincode = Pincode)
    print(queryset_list,request.GET['pincode'])
    
    for result in queryset_list:
        State_result = States[result.State-1][1]
       # dept_result = Department[result.Department-1][1]
    context = {
        'States' : State_result,
        #'Department' : dept_result,
        'results' : queryset_list,
        'values' : request.GET
    }
    

    return render(request, 'hosSearchResults.html', context)