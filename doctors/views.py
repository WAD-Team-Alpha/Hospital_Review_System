from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404
from .models import Doctor
from accounts.models import User
from reviews.models import DocReview
from .choices import Department, States
# Create your views here.


def docProf(request, doctor_id):
    doctor =get_object_or_404(Doctor, pk= doctor_id)
    queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)
    
    five_stars = 0
    for review  in queryset_list:
        if review.star_rating == "12345":
            five_stars = five_stars + 1
    four_stars = 0
    for review  in queryset_list:
        if review.star_rating == "1234":
            four_stars = four_stars + 1
    three_stars = 0
    for review  in queryset_list:
        if review.star_rating == "123":
            three_stars = three_stars + 1
    two_stars = 0
    for review  in queryset_list:
        if review.star_rating == "12":
            two_stars = two_stars + 1
    one_stars = 0
    for review  in queryset_list:
        if review.star_rating == "1":
            one_stars = one_stars + 1
    #percentages
    count = doctor.Ratings_count
    if count != 0:
        five_starPercentage = five_stars/count*100
        four_starPercentage = four_stars/count*100
        three_starPercentage = three_stars/count*100
        two_starPercentage = two_stars/count*100
        one_starPercentage = one_stars/count*100
    else:
        five_starPercentage = 0
        four_starPercentage = 0
        three_starPercentage = 0
        two_starPercentage = 0
        one_starPercentage = 0


    
   
    ratings_count = {
        "five_star" : five_stars,
        "four_star" : four_stars,
        "three_star" : three_stars,
        "two_star" : two_stars,
        "one_star" : one_stars,
    }
    ratings_percentage = {
        "five_starPercentage" : five_starPercentage,
        "four_starPercentage" : four_starPercentage,
        "three_starPercentage" : three_starPercentage,
        "two_starPercentage" : two_starPercentage,
        "one_starPercentage" : one_starPercentage,
    
    }
    
    queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)[:3]
    flag = 0
    if request.method == 'POST':
        flag = 1
        queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)
    context = {
        'doctor' : doctor,
        'doctor_reviews' : queryset_list,
        'flag' : flag,
        'ratings_count' : ratings_count,
        'ratings_percentage' : ratings_percentage,
        
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