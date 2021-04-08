from django.contrib import admin
from .models import DocReview
from .models import HosReview
# Register your models here.
class DocReviewAdmin(admin.ModelAdmin):
    list_display = ('id','doctor', 'user','rating')
    
admin.site.register( DocReview ,DocReviewAdmin)

class HosReviewAdmin(admin.ModelAdmin):
    list_display = ('id','hospital', 'user','rating')
    
admin.site.register( HosReview ,HosReviewAdmin)