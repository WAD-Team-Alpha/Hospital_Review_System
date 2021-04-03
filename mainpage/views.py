from django.shortcuts import render
from accounts.models import User
from doctors.models import Doctor
# Create your views here.
def index(request):
    users = User.objects.order_by('Username')
    context = {
        'users' : users
    }
    return render(request, 'index.html')
