from django import forms
from .models import *
from .choices import *

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {"FirstName", "LastName", "Email", "Username", "DateOfBirth", "MobileNumber"}
        widgets = {
            "FirstName": forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'fname',
                    'name': 'fname',
                    'placeholder': 'First Name',
                    'required': True
                }
            ), 
            "LastName": forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'lname',
                    'name': 'lname',
                    'placeholder': 'Last Name',
                    'required': True
                }
            ), 
            "Username": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'username',
                'name': 'Username',
                'placeholder': 'Username',
                'required': True
            }),
            "Email": forms.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'id': 'reg_email',
                    'name': 'email',
                    'placeholder': 'Your Email',
                    'required': True
                }
            ), 
            "DateOfBirth": forms.DateInput(
                attrs={
                    'type': 'date',
                    'name': 'date',
                    'value': '',
                    'class': 'form-control',
                    'required': True
                }
            ), 
            "MobileNumber": forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'mobile-num',
                    'name': 'm-num',
                    'placeholder': '+91 ',
                    'required': True
                }
            )
        }