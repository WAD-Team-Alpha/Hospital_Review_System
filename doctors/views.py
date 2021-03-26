from django.shortcuts import render

# Create your views here.

def docProf(request):
    return render(request, 'DoctorProfile.html')
def searchRes(request):
    return render(request, 'searchbarResults.html')