from django.shortcuts import render, get_object_or_404
from .models import Hospital
from doctors.models import Doctor
from accounts.models import User
from reviews.models import HosReview
from .choices import States

# Create your views here.
def hosProf(request, hospital_id):
    '''
    this function will helps the hospital profile html page to access all the dynamic data 
    from the database. we get hospital_id from html page
    '''

    #checking whether doctor  exists or not
    hospital =get_object_or_404(Hospital, pk= hospital_id)
    doctor_list = Doctor.objects.all().filter(HospitalRegisterationNumber=hospital.HospitalRegisterationNumber)
    print(doctor_list)
    queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)
    
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
    count = hospital.Ratings_count
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
    queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)[:3]
    flag = 0
    if request.method == 'POST':
        flag = 1
        queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)

    # sending all the computed values to the to context
    context = {
        'hospital' : hospital,
        'hospital_reviews' : queryset_list,
        'flag' : flag,
        'ratings_count' : ratings_count,
        'ratings_percentage' : ratings_percentage,
        'doctors' : doctor_list
    }
    return render(request, 'HospitalProfile.html', context)

def hosSearch(request):
    queryset_list = Hospital.objects.order_by('-HospitalName')
    State_result = States
    print(State_result)

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
   
    if 'state' in request.GET:
        if not request.GET['state'] == "29":
            State = request.GET['state']
            if State:
                queryset_list = queryset_list.filter(State = State)

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
        res={
            'result': Result,
            'State_result' : State_result,
        }
        dict.append(res)
    
        
            
    context = {
        'dict': dict
    }
    

    return render(request, 'hosSearchResults.html', context)