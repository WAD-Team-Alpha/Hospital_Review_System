from django.shortcuts import render

# Create your views here.
def hosProf(request):
    return render(request, 'HospitalProfile.html')