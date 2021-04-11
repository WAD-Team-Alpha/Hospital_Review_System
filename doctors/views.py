from django.shortcuts import render, get_object_or_404
from .models import Doctor
from accounts.models import User
from reviews.models import DocReview
from .choices import Department, States
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
    queryset_list = Doctor.objects.order_by('-FirstName')
    State_result = States
    print(State_result)
    dept_result = Department

    #firstname

    if 'first_name' in request.GET:
        FirstName = request.GET['first_name']
        if FirstName:
            queryset_list = queryset_list.filter(FirstName__iexact = FirstName)
          
    #print(queryset_list)  
    
    #lastname
    if 'last_name' in request.GET:
        LastName = request.GET['last_name']
        if LastName:
            queryset_list = queryset_list.filter(LastName__iexact = LastName)
    #print(queryset_list)  
    
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
     
    #Department
    if 'dept' in request.GET:
        Departments = request.GET['dept']
        if Departments:
            queryset_list = queryset_list.filter(Department = Departments)
    print(queryset_list,request.GET['dept']) 
    #pincode
    if 'pincode' in request.GET:
         Pincode = request.GET['pincode']
         if Pincode:
             queryset_list = queryset_list.filter(Pincode = Pincode)
    print(queryset_list,request.GET['pincode'])
    
    for result in queryset_list:
        State_result = States[result.State-1][1]
        dept_result = Department[result.Department-1][1]
    context = {
        'States' : State_result,
        'Department' : dept_result,
        'results' : queryset_list,
        'values' : request.GET
    }
    

    return render(request, 'searchbarResults.html', context)