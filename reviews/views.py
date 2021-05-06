from hospitals.models import Hospital
from django.shortcuts import render, redirect
from doctors.models import Doctor
from accounts.models import User
from .models import DocReview
from .models import HosReview
from django.contrib import messages
# Create your views here.


def docreview(request):
    '''
    This function is used to add review to doctor reviews database and then updates the html file,
    if only if user get logged in with a user account and added review.
    '''
    # checking wether it is post or not.
    if request.method == 'POST':
        # accessing values using post method.
        doctor_id = request.POST['doctor_id']
        doctor_name = request.POST['doctor_name']

        #checking whether user is logged in or not
        if not request.user.is_authenticated:
            return redirect('signin')
        
        #using try to make sure that user entered valid inputs in reviews    
        try:
            username = request.POST['username']
            star_rating = request.POST['rating']
        except:
            # if this run only when user din't give the ratings value in html page
            return redirect('/doctors/'+doctor_id)

        non_rating = "" #non_rating used for html page porpose
        # updating non_rating based on star_rating
        if star_rating == '1':
            non_rating = "2345"
        elif star_rating == '12':
            non_rating = "345"
        elif star_rating == '123':
            non_rating = "45"
        elif star_rating == '1234':
            non_rating = "5"
        elif star_rating == '12345':
            non_rating = ""
        review = request.POST['review']
        
        # checking whether user found in Users table
        try:
           user = User.objects.all().filter(Username=request.user.username).get()
        except:
            # if this run only when user signed in with non user account
            messages.error(request, "You are not eligible to add review")
            return redirect('/doctors/'+doctor_id)
        
        doctor = Doctor.objects.all().filter(Username=doctor_name).get()
        # adding review to database
        reviewed = DocReview(doctor=doctor, user=user, star_rating=star_rating,non_rating=non_rating, review=review)
        reviewed.save()
        # filtering all the reviews of the target doctor
        queryset_list = DocReview.objects.order_by('-review_date').filter(doctor = doctor)
        
        # from here we update average rating, number of ratings and also star_ratings and non_ratings
        # in doctor database 
        avg = []
        length = 0
        for doctor in queryset_list:
            length = length + 1 
            avg.append(len(doctor.star_rating))  
        
        avg = sum(avg)/len(avg)
        # print(avg)
        stars = ""
        non_stars = "12345"
        if avg > 4.5:
            stars = "12345"
            non_stars = ""
        elif avg > 3.5:
            stars = "1234"
            non_stars = "1"
        elif avg > 2.5:
            stars = "123"
            non_stars = "12"
        elif avg > 1.5:
            stars = "12"
            non_stars = "123"
        elif avg > 0.5:
            stars = "1"
            non_stars = "1234"
        # updating the values 
        doctor = Doctor.objects.all().filter(Username=doctor_name).update(Rating = avg,Ratings_stars = stars,Ratings_count = length,non_stars = non_stars)
        messages.success(request, "Added review sucessfully")
        return redirect('/doctors/'+doctor_id)
def hosreview(request):
    '''
    This function is used to add review to hospital reviews database and then updates the html file,
    if only if user get logged in with a user account and added review.
    '''
      # checking wether it is post or not.
    if request.method == 'POST':
        # accessing values using post method.
        hospital_id = request.POST['hospital_id']
        hospital_name = request.POST['hospital_name']
        #checking whether user is logged in or not
        if not request.user.is_authenticated:
            return redirect('signin')

        #using try to make sure that user entered valid inputs in reviews
        try:
            username = request.POST['username']
            star_rating = request.POST['rating']
        except:
           # if this run only when user din't give the ratings value in html page
            return redirect('/hospitals/'+hospital_id)
        non_rating = "" #non_rating used for html page porpose
        # updating non_rating based on star_rating
        if star_rating == '1':
            non_rating = "2345"
        elif star_rating == '12':
            non_rating = "345"
        elif star_rating == '123':
            non_rating = "45"
        elif star_rating == '1234':
            non_rating = "5"
        elif star_rating == '12345':
            non_rating = ""
        review = request.POST['review']
        
        # checking whether user found in Users table
        try:
            user = User.objects.all().filter(Username=request.user.username).get()
        except:
            # if this run only when user signed in with non user account
            messages.error(request, "You are not eligible to add review")
            return redirect('/hospitals/'+hospital_id)
        
        hospital = Hospital.objects.all().filter(Username=hospital_name).get()
        # adding review to database
        reviewed = HosReview(hospital=hospital, user=user, star_rating=star_rating,non_rating=non_rating, review=review)
        reviewed.save()
        # filtering all the reviews of the target hospital
        queryset_list = HosReview.objects.order_by('-review_date').filter(hospital = hospital)
        
        # from here we update average rating, number of ratings and also star_ratings and non_ratings
        # in hospital database 
        avg = []
        length = 0
        for hospital in queryset_list:
            length = length + 1 
            avg.append(len(hospital.star_rating))  
        
        avg = sum(avg)/len(avg)
        # print(avg)
        stars = ""
        non_stars = "12345"
        if avg > 4.5:
            stars = "12345"
            non_stars = ""
        elif avg > 3.5:
            stars = "1234"
            non_stars = "1"
        elif avg > 2.5:
            stars = "123"
            non_stars = "12"
        elif avg > 1.5:
            stars = "12"
            non_stars = "123"
        elif avg > 0.5:
            stars = "1"
            non_stars = "1234"
        # updating the values 
        hospital = Hospital.objects.all().filter(Username=hospital_name).update(Rating = avg,Ratings_stars = stars,Ratings_count = length,non_stars = non_stars)
        messages.success(request, "Added review sucessfully")
        return redirect('/hospitals/'+hospital_id)


