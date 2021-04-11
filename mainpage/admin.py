from django.contrib import admin
from .models import Appointment

# Register your models here.

class MainPageAdmin(admin.ModelAdmin):
    list_display = ("user", "doctor", "dateOfAppointment", "AdditionalMessage")
    
admin.site.register( Appointment , MainPageAdmin)