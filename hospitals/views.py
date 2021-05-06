import doctors
from django.shortcuts import render, get_object_or_404
from .models import Hospital
from doctors.models import Doctor
from accounts.models import User
from reviews.models import HosReview
from .choices import States
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
# Create  Hospital profile function 

def hosProf(request, hospital_id):
    '''
    this function will helps the hospital profile html page to access all the dynamic data 
    from the database. we get hospital_id from html page
    '''

    #checking whether doctor  exists or not
    hospital =get_object_or_404(Hospital, pk= hospital_id)
    # doctor search list which belong to this hospital 
    doctor_list = Doctor.objects.all().filter(HospitalRegisterationNumber=hospital.HospitalRegisterationNumber)
    # print(doctor_list)
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
   
# Hospital search result  function 


# Hospital Search Results Function
def hosSearch(request):
    #Storing all the objects of the hospital which are imported from models in queryset_list and are ordered by their FirstName
    queryset_list = Hospital.objects.order_by('-HospitalName')
    #Assigning variable State_result for the States which are imported from choices
    State_result = States
    # print(State_result)

    #firstname
    #Getting hospital name from user Search for hospital
    if 'first_name' in request.GET:
        #Storing first_name in HospitalName
         HospitalName = request.GET['first_name']
         #if HospitalName exists then we are filtering the required HospitalName from database and storing it in queryset_list and __iexact is used for case insensitive match for HospitalName.
         if HospitalName:
             queryset_list = queryset_list.filter(HospitalName__iexact = HospitalName)
          
    # print(queryset_list)  
    
    #lastname
    if 'last_name' in request.GET:
        RegNo = request.GET['last_name']
        if RegNo:
            queryset_list = queryset_list.filter(HospitalRegisterationNumber__iexact = RegNo)
    # print(queryset_list)  
    
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
    # print(queryset_list,request.GET['pincode'])
    
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

def updateProf(request):
    '''
     This function takes the input from the update hospital html page and updates the database
     and then redirect to the profile page.
    '''
    if request.method == "POST":
        flag1 = 0
        flag2 = 0
        flag3 = 0
        data = request.POST
        files1 = request.FILES.get('profilePhoto')
        files2 = request.FILES.get('chiefPhoto')
        files3 = request.FILES.get('chiefcertificate')

        fs = FileSystemStorage()

        try:
            fs.save("HospitalPhotos/"+files1.name, files1)
            Path1 = "HospitalPhotos/"+str(files1.name)
        except AttributeError:
            flag1 = 1
        try:
            fs.save("ChiefDoctorPhotos/"+files2.name, files2)
            Path2 = "ChiefDoctorPhotos/"+str(files2.name)
        except AttributeError:
            flag2 = 1
        try:
            fs.save("ChiefDoctorDocuments/"+files3.name, files3)
            Path3 = "ChiefDoctorDocuments/"+str(files3.name)
        except AttributeError:
            flag3 = 1

        hospital = Hospital.objects.all().filter(Username=request.user.username).get()

        if data['hospitalName'] == "":
            hosname = hospital.HospitalName
        else:
            hosname = data['hospitalName']

        if data['hosRegNo'] == "":
            hosRegNo = hospital.HospitalRegisterationNumber
        else:
            hosRegNo = data['hosRegNo']

        if flag1 == 0:
            profilePhoto = Path1
        else:
            profilePhoto = hospital.HospitalPhoto
        if flag3 == 0:
            cmoc = Path3
        else:
            cmoc = hospital.ChiefMedicalOfficerCertificate
        if flag2 == 0:
            cmop = Path2
        else:
            cmop = hospital.ChiefMedicalOfficerPhoto

        if data['phn_no'] == "":
            mobilenum = hospital.PhoneNumber
        else:
            mobilenum = data['phn_no']

        if data['hosDesc'] == "":
            hosDesc = hospital.HospitalDescription
        else:
            hosDesc = data['hosDesc']

        if data['town'] == "":
            town = hospital.Town
        else:
            town = data['town']

        if data['city'] == "":
            city = hospital.City
        else:
            city = data['city']

        if data['state'] == '0':
            state = hospital.State
        else:
            state = data['state']

        if data['pinc'] == "":
            pincode = hospital.Pincode
        else:
            pincode = data['pinc']

        if data['cmo'] == "":
            cmo = hospital.ChiefMedicalOfficer
        else:
            cmo = data['cmo']
        
        if data['cmod'] == "":
            cmod = hospital.CheifMedicalOfficerDescription
        else:
            cmod = data['cmod']
        

        if data['ach1'] == "":
            ach1 = hospital.Achievements1
        else:
            ach1 = data['ach1']

        if data['ach2'] == "":
            ach2 = hospital.Achievements2
        else:
            ach2 = data['ach2']

        if data['ach3'] == "":
            ach3 = hospital.Achievements3
        else:
            ach3 = data['ach3']

        if data['ach4'] == "":
            ach4 = hospital.Achievements4
        else:
            ach4 = data['ach4']
        if data['ach5'] == "":
            ach5 = hospital.Achievements5
        else:
            ach5 = data['ach5']
        if data['ach6'] == "":
            ach6 = hospital.Achievements6
        else:
            ach6 = data['ach6']

        #updating the data base
        hospitalUpdated = Hospital.objects.all().filter(Username=request.user.username).update(
            HospitalPhoto = profilePhoto,      
            HospitalName = hosname,
            HospitalRegisterationNumber = hosRegNo,
            City = city,
            Town = town,
            State = state,
            Pincode = pincode,
            ChiefMedicalOfficer = cmo,
            ChiefMedicalOfficerCertificate = cmoc,
            ChiefMedicalOfficerPhoto = cmop,
            CheifMedicalOfficerDescription = cmod,
            PhoneNumber =  mobilenum,
            HospitalDescription = hosDesc,
            Achievements1 = ach1,
            Achievements2 = ach2,
            Achievements3 = ach3,
            Achievements4 = ach4,
            Achievements5 = ach5,
            Achievements6 = ach6,
        )
        hospital_id = str(hospital.id)
        messages.success(request, "Updated profile sucessfully")
        return redirect('/hospitals/'+hospital_id )
        
    return render(request, 'hospitalUpdateProfile.html')
