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

    dept = Department[doctor.Department-1][1]

    context = {
        'doctor' : doctor,
        'doctor_reviews' : queryset_list,
        'flag' : flag,
        'ratings_count' : ratings_count,
        'ratings_percentage' : ratings_percentage,
        'department': dept,
    }
    return render(request, 'DoctorProfile.html', context)


# Doctor Search Results Function
def searchRes(request):
    #Storing all the objects of the Doctor which are imported from models in queryset_list and are ordered by their FirstName
    queryset_list = Doctor.objects.order_by('-FirstName')

    #Assigning variable State_result for the States which are imported from choices
    State_result = States
    

    #Assigning variable dept_result for the Department which are imported from choices
    dept_result = Department

    #firstname
    #Getting first_name from user Search for Doctor
    if 'first_name' in request.GET:
        #Storing first_name in FirstName
        FirstName = request.GET['first_name']
        #if FirstName exists then we are filtering the required FirstName from database and storing it in queryset_list and __iexact is used for case insensitive match for FirstName.
        if FirstName:
            queryset_list = queryset_list.filter(FirstName__iexact = FirstName)
          
    
    
    #lastname
    #Getting last_name from user Search for Doctor
    if 'last_name' in request.GET:
        #Storing last_name in LastName
        LastName = request.GET['last_name']
        #if LastName exists then we are filtering the required LastName from database and storing it in queryset_list and __iexact is used for case insensitive match for  LastName.
        if LastName:
            queryset_list = queryset_list.filter(LastName__iexact = LastName)
  
    
    #City
    #Getting city from user Search for Doctor
    if 'city' in request.GET:
        #Storing city in City
        City = request.GET['city']
         #if City exists then we are filtering the required City from database and storing it in queryset_list and __iexact is used for case insensitive match for City.
        if City:
            queryset_list = queryset_list.filter(City__iexact = City)
     
    
    #State
    #Getting State from User Search for Doctor
    if 'state' in request.GET:
        #if the searched option is not equal to All i.e. if User select any other state than All then we're storing the state in State variable and filtering the required State from database.
        #If user selects All then we dont filter any states and pass.
        if not request.GET['state'] == "29":
            State = request.GET['state']
            if State:
                queryset_list = queryset_list.filter(State = State)
          
    #Department
    #Getting Department from User Search for Doctor
    if 'dept' in request.GET:
        #if the searched option is not equal to All i.e. if User selects any other department than All then we're storing the department in Departments variable and filtering the required Department from database.
        #If user selects All then we dont filter any Department and pass.
        if not request.GET['dept'] == "7":
            Departments = request.GET['dept']
            if Departments:
                queryset_list = queryset_list.filter(Department = Departments)
   
    #pincode
    #Getting pincode from User Search for Doctor
    if 'pincode' in request.GET:
         #Storing pincode in Pincode
         Pincode = request.GET['pincode']
         #if Pincode exists then we are filtering the required pincode from database and storing it in queryset_list.
         if Pincode:
             queryset_list = queryset_list.filter(Pincode = Pincode)
    
    
    #Declaring empty list dict for storing the results based on user search because if User searches with All option we need to store each doctor search result from each state in a list to show search results.
    dict = []
    for result in queryset_list:
        Result = result
        #Extarcting Key value for the State and Deaprtment from choices.py 
        State_result = States[result.State-1][1]
        dept_result = Department[result.Department-1][1]
        #Storing the above three values in a Dictionary
        res={
            'result': Result,
            'State_result' : State_result,
            'dept_result': dept_result,
        }
        #Appending res to dict.
        dict.append(res)
    
        
    #Passing dict values in context        
    context = {
        'dict': dict
    }
    #Passing values of context to Doctor Search Results page
    return render(request, 'searchbarResults.html', context)