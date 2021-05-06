from django.contrib import messages
import doctors
from os import error
from django.core.files.storage import FileSystemStorage
from django.db.models.aggregates import Count
from django.shortcuts import redirect, render, get_object_or_404
from .models import Doctor
from accounts.models import User
from reviews.models import DocReview
from .choices import Department, States
# Create your views here.

# Doctor profile view function  
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
    exp = ""
    if doctor.YearsOfExperience == 0:
        exp = "Not given about no. of"
    else:
        exp = doctor.YearsOfExperience

    context = {
        'doctor' : doctor,
        'doctor_reviews' : queryset_list,
        'flag' : flag,
        'ratings_count' : ratings_count,
        'ratings_percentage' : ratings_percentage,
        'department': dept,
        'experience': exp,
    }
    return render(request, 'DoctorProfile.html', context)



# it is doctor search result by user get all details

def searchRes(request):
    queryset_list = Doctor.objects.order_by('-FirstName')
    State_result = States
    # print(State_result)
    dept_result = Department

    #firstname

    if 'first_name' in request.GET:
        FirstName = request.GET['first_name']
        if FirstName:
            queryset_list = queryset_list.filter(FirstName__iexact = FirstName)
          
    ## print(queryset_list)  
    
    #lastname
    if 'last_name' in request.GET:
        LastName = request.GET['last_name']
        if LastName:
            queryset_list = queryset_list.filter(LastName__iexact = LastName)
    ## print(queryset_list)  
    
    #town/village
    if 'place' in request.GET:
        Town = request.GET['place']
        if Town:
            queryset_list = queryset_list.filter(Town__iexact = Town)
    # print(queryset_list)  
    #City
    if 'city' in request.GET:
        City = request.GET['city']
        if City:
            queryset_list = queryset_list.filter(City__iexact = City)
    # print(queryset_list,request.GET['city'])  
    #State

    if 'state' in request.GET:
        if not request.GET['state'] == "29":
            State = request.GET['state']
            if State:
                queryset_list = queryset_list.filter(State = State)
          
    #Department of doctor 
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
    # print(queryset_list,request.GET['pincode'])
    
   
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

def updateProf(request):
    if request.method == "POST":
        flag = 0
        data = request.POST
        files = request.FILES.get('profilePhoto')
        fs = FileSystemStorage()

        try:
            fs.save("DoctorPhotos/"+files.name, files)
            Path = "DoctorPhotos/"+str(files.name)
        except AttributeError:
            flag = 1


        doctor = Doctor.objects.all().filter(Username=request.user.username).get()

        if data['fname'] == "":
            fname = doctor.FirstName
        else:
            fname = data['fname']

        if data['lname'] == "":
            lname = doctor.LastName
        else:
            lname = data['lname']

        if flag == 0:
            profilePhoto = Path
        else:
            profilePhoto = doctor.ProfilePhoto

        if data['phn_no'] == "":
            mobilenum = doctor.MobileNumber
        else:
            mobilenum = data['phn_no']

        if data['yoe'] == "":
            yoe = doctor.YearsOfExperience
        else:
            yoe = data['yoe']

        if data['hospname'] == "":
            hospname = doctor.HospitalName
        else:
            hospname = data['hospname']

        if data['hospRegNum'] == "":
            hospRegNum = doctor.HospitalRegisterationNumber
        else:
            hospRegNum = data['hospRegNum']

        if data['city'] == "":
            city = doctor.City
        else:
            city = data['city']

        if data['state'] == "":
            state = doctor.State
        else:
            state = data['state']

        if data['pinc'] == "":
            pincode = doctor.Pincode
        else:
            pincode = data['pinc']

        if data['dept'] == "":
            dept = doctor.Department
        else:
            dept = data['dept']

        if data['desc'] == "":
            desc = doctor.Description
        else:
            desc = data['desc']

        if data['ach1'] == "":
            ach1 = doctor.Achievements1
        else:
            ach1 = data['ach1']

        if data['ach2'] == "":
            ach2 = doctor.Achievements2
        else:
            ach2 = data['ach2']

        if data['ach3'] == "":
            ach3 = doctor.Achievements3
        else:
            ach3 = data['ach3']

        if data['ach4'] == "":
            ach4 = doctor.Achievements4
        else:
            ach4 = data['ach4']

        doctorUpdated = Doctor.objects.all().filter(Username=request.user.username).update(
            FirstName = fname,
            LastName = lname,
            ProfilePhoto = profilePhoto,
            MobileNumber = mobilenum,
            YearsOfExperience = yoe ,          
            HospitalName = hospname,
            HospitalRegisterationNumber = hospRegNum,
            City = city,
            State = state,
            Pincode = pincode,
            Department = dept,
            Description = desc,
            Achievements1 = ach1,
            Achievements2 = ach2,
            Achievements3 = ach3,
            Achievements4 = ach4
        )

        messages.success(request, "Updated profile sucessfully")
        return redirect('index')
        
    return render(request, 'doctorUpdateProfile.html')