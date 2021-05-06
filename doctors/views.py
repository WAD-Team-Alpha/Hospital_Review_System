from django.db.models.aggregates import Count
from django.shortcuts import render, get_object_or_404
from .models import Doctor
from accounts.models import User
from reviews.models import DocReview
from .choices import Department, States
# Create your views here.


def docProf(request, doctor_id):
    '''
    this function will helps the doctor profile html page to access all the dynamic data 
    from the database. we get doctor_id from html page
    '''
    #checking whether doctor  exists or not
    doctor =get_object_or_404(Doctor, pk= doctor_id)
    queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)
    
    # computing the count of each type of stars 
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

    #computing percentages of each star belogs to.
    count = doctor.Ratings_count
    if count != 0:
        five_starPercentage = five_stars/count*100
        four_starPercentage = four_stars/count*100
        three_starPercentage = three_stars/count*100
        two_starPercentage = two_stars/count*100
        one_starPercentage = one_stars/count*100
    else:
        # this will run when no reviews are added as count = 0
        five_starPercentage = 0
        four_starPercentage = 0
        three_starPercentage = 0
        two_starPercentage = 0
        one_starPercentage = 0


    
    # storing all counts in a ratings_count dictcionary
    ratings_count = {
        "five_star" : five_stars,
        "four_star" : four_stars,
        "three_star" : three_stars,
        "two_star" : two_stars,
        "one_star" : one_stars,
    }

    # storing all counts in a ratings_percentage dictcionary
    ratings_percentage = {
        "five_starPercentage" : five_starPercentage,
        "four_starPercentage" : four_starPercentage,
        "three_starPercentage" : three_starPercentage,
        "two_starPercentage" : two_starPercentage,
        "one_starPercentage" : one_starPercentage,
    
    }
    
    # here flag is used to decide whether to send all the reviews or only 3 reviews
    #by default(flag = 0) we send only 3 reviews until user request for more (flag = 1)
    queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)[:3]
    flag = 0 
    if request.method == 'POST':
        flag = 1
        queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)

    dept = Department[doctor.Department-1][1]

    # sending all the computed values to the to context
    context = {
        'doctor' : doctor,
        'doctor_reviews' : queryset_list,
        'flag' : flag,
        'ratings_count' : ratings_count,
        'ratings_percentage' : ratings_percentage,
        'department': dept,
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
        if not request.GET['state'] == "29":
            State = request.GET['state']
            if State:
                queryset_list = queryset_list.filter(State = State)
          
    #Department
    if 'dept' in request.GET:
        if not request.GET['dept'] == "7":
            Departments = request.GET['dept']
            if Departments:
                queryset_list = queryset_list.filter(Department = Departments)
   
    #pincode
    if 'pincode' in request.GET:
         Pincode = request.GET['pincode']
         if Pincode:
             queryset_list = queryset_list.filter(Pincode = Pincode)
    print(queryset_list,request.GET['pincode'])
    
   
    dict = []
    for result in queryset_list:
        Result = result
        State_result = States[result.State-1][1]
        dept_result = Department[result.Department-1][1]
        res={
            'result': Result,
            'State_result' : State_result,
            'dept_result': dept_result,
        }
        dict.append(res)
    
        
            
    context = {
        'dict': dict
    }
    return render(request, 'searchbarResults.html', context)