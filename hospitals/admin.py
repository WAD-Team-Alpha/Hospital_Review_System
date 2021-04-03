from django.contrib import admin
from .models import Hospital
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'HospitalName', 'Username')
    
admin.site.register( Hospital ,HospitalAdmin)