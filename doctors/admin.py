from django.contrib import admin
from .models import Doctor
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'Username', 'Email')
    
admin.site.register( Doctor ,DoctorAdmin)