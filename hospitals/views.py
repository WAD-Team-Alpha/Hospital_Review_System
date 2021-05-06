from django.shortcuts import render, get_object_or_404
from .models import Hospital
from doctors.models import Doctor
from accounts.models import User
from reviews.models import HosReview
from .choices import States

# Create your views here.
def hosProf(request, hospital_id):
    hospital =get_object_or_404(Hospital, pk= hospital_id)
    doctor_list = Doctor.objects.all().filter(HospitalRegisterationNumber=hospital.HospitalRegisterationNumber)
    print(doctor_list)
    queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)
    
    
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
    count = hospital.Ratings_count
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
    queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)[:3]
    flag = 0
    if request.method == 'POST':
        flag = 1
        queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)
    context = {
        'hospital' : hospital,
        'hospital_reviews' : queryset_list,
        'flag' : flag,
        'ratings_count' : ratings_count,
        'ratings_percentage' : ratings_percentage,
        'doctors' : doctor_list
    }
    return render(request, 'HospitalProfile.html', context)

# Hospital Search Results Function
def hosSearch(request):
    #Storing all the objects of the hospital which are imported from models in queryset_list and are ordered by their FirstName
    queryset_list = Hospital.objects.order_by('-HospitalName')
    #Assigning variable State_result for the States which are imported from choices
    State_result = States
    print(State_result)

    #firstname
    #Getting hospital name from user Search for hospital
    if 'first_name' in request.GET:
        #Storing first_name in HospitalName
         HospitalName = request.GET['first_name']
         #if HospitalName exists then we are filtering the required HospitalName from database and storing it in queryset_list and __iexact is used for case insensitive match for HospitalName.
         if HospitalName:
             queryset_list = queryset_list.filter(HospitalName__iexact = HospitalName)
          
    #print(queryset_list)  
    
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
   
   #state
    if 'state' in request.GET:
        if not request.GET['state'] == "29": #this line is for the option 'all'
            State = request.GET['state']
            if State:
                queryset_list = queryset_list.filter(State = State)

    #pincode
    if 'pincode' in request.GET:
         Pincode = request.GET['pincode']
         if Pincode:
             queryset_list = queryset_list.filter(Pincode = Pincode)
    print(queryset_list,request.GET['pincode'])
    
    #Declaring empty list dict for storing the results based on user search because if User searches with 'All' option we need to store each doctor search result from each state in a list to show search results.
    dict = []
    for result in queryset_list:
        Result = result
         #Extarcting Key value for the State from choices.py 
        State_result = States[result.State-1][1]
        #Storing the above two values in a Dictionary
        res={
            'result': Result,
            'State_result' : State_result,
        }
        #Appending res to dict.
        dict.append(res)
    
        
    #Passing dict values in context        
    context = {
        'dict': dict
    }
    
    #Passing values of context to Doctor Search Results page
    return render(request, 'hosSearchResults.html', context)