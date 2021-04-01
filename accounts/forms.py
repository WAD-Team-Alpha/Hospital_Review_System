from django import forms
from .models import *
from .choices import *

class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = {"FirstName", "LastName", "Email", "DateOfBirth", "MobileNumber"}
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

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctors
        fields = ["FirstName", "LastName", "HospitalName", "Email", "Education", "DoctorLicense", "Description", "Department", "DateOfBirth", 
                  "Achievements4", "Achievements3", "Achievements2", "Achievements1", "YearsOfExperience", "Masters", "MobileNumber"]
        widgets = {
            "FirstName": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'fname',
                'name': 'fname',
                'placeholder': 'First Name',
                'required': True
            }), 
            "LastName": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'lname',
                'name': 'lname',
                'placeholder': 'Last Name',
                'required': True
            }), 
            "Email": forms.EmailInput(attrs={
                'type': 'email',
                'class': 'form-control',
                'id': 'reg_email',
                'name': 'email',
                'placeholder': 'Your Email',
                'required': True
            }), 
            "HospitalName": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'fname',
                'name': 'fname',
                'placeholder': 'First Name',
                'required': True
            }), 
            "Education": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'education',
                'name': 'education',
                'placeholder': 'Education',
                'required': False
            }), 
            "DoctorLicense": forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'attach',
                'name': 'cs',
                'placeholder': 'Here',
                'required': True
            }), 
            "Description": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'status',
                'name': 'status',
                'placeholder': 'About Yourself Here .',
                'required': False
            }), 
            "Department": forms.Select(attrs={
                'class': 'form-control',
                'name': 'department',
                'choices': Department,
                'required': True
            }), 
            "DateOfBirth": forms.DateInput(attrs={
                'type': 'date',
                'name': 'date',
                'value': '',
                'class': 'form-control',
                'required': True
            }), 
            "Masters": forms.TextInput(attrs={
                'type': 'date',
                'name': 'master',
                'id': 'master',
                'value': '',
                'placeholder': 'Place where you studied Masters',
                'class': 'form-control',
                'required': False
            }), 
            "YearsOfExperience": forms.NumberInput(attrs={
                'type': 'number',
                'name': 'yoe',
                'id': 'attach',
                'placeholder': 'Here',
                'class': 'form-control',
                'required': True
            }), 
            "Achievements1": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach_1',
                'name': 'ach1',
                'placeholder': '1.'
            }), 
            "Achievements2":forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach_2',
                'name': 'ach2',
                'placeholder': '2.'
            }), 
            "Achievements3": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach_3',
                'name': 'ach3',
                'placeholder': '3.'
            }), 
            "Achievements4": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach_4',
                'name': 'ach4',
                'placeholder': '4.'
            }), 
            "MobileNumber": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'mobile-num',
                'name': 'm-num',
                'placeholder': '+91 ',
                'required': True
            })
        }