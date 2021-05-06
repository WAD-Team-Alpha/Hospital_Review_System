from django import forms
from .models import *
from .choices import *
#Create doctor profile forms

class HospitalForm(forms.ModelForm):
        # All attributes  from models forms for user input 
    class Meta:
        model = Hospital
        fields = ["HospitalName", "HospitalRegisterationNumber", "HospitalLicense", "HospitalPhoto", 
                "Username", "Email", "HospitalEshtablishDate", "HospitalDescription", "Town", "City", "Pincode", 
                "State", "ChiefMedicalOfficer", "ChiefMedicalOfficerCertificate", "ChiefMedicalOfficerPhoto",
                "CheifMedicalOfficerDescription", "PhoneNumber", "Achievements1", "Achievements2", 
                "Achievements3", "Achievements4", "Achievements5", "Achievements6"]
         # All details for each attributes
        widgets = {
            "HospitalName": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'hospName',
                'name': 'hospName',
                'placeholder': 'Hospital Name',
                'required': True
            }), 
            "HospitalRegisterationNumber": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'hospRegNum',
                'name': 'hospRegNum',
                'placeholder': 'Hospital Registration Number',
                'required': True
            }), 
            "HospitalLicense": forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'license',
                'name': 'license',
                'placeholder': 'here',
                'required': True
            }), 
            "HospitalPhoto": forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'hospPhoto',
                'name': 'hospPhoto',
                'placeholder': 'here',
                'required': False
            }), 
            "Username": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'username',
                'name': 'username',
                'placeholder': 'Username',
                'required': True
            }),
            "Email": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Enter Email',
                'required': True
            }), 
            "HospitalEshtablishDate": forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'estDate',
                'name': 'estDate',
                'placeholder': 'here',
                'required': True
            }), 
            "HospitalDescription": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'hospDesc',
                'name': 'hospDesc',
                'placeholder': 'Hospital Description',
                'required': False
            }), 
            "Town": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'town',
                'name': 'town',
                'placeholder': 'Town',
                'required': True
            }), 
            "City": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'city',
                'name': 'city',
                'placeholder': 'City',
                'required': True
            }), 
            "Pincode": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'pincode',
                'name': 'pincode',
                'placeholder': 'Pincode',
                'required': True
            }), 
            "State": forms.Select(attrs={
                'class': 'form-control',
                'name': 'State',
                'choices': States,
                'required': True
            }), 
            "ChiefMedicalOfficer": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'chiefDoc',
                'name': 'chiefDoc',
                'placeholder': 'Name of cheif Doctor in Hospital',
                'required': True
            }), 
            "ChiefMedicalOfficerCertificate": forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'chiefDocCertificate',
                'name': 'chiefDocCertificate',
                'placeholder': 'here',
                'required': True
            }), 
            "ChiefMedicalOfficerPhoto": forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'chiefDocPhoto',
                'name': 'chiefDocPhoto',
                'placeholder': 'here',
                'required': False
            }),
            "CheifMedicalOfficerDescription": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'chiefDocDescription',
                'name': 'Description for Chief Doctor',
                'placeholder': 'Some info. about the chief Doctor',
                'required': False
            }), 
            "PhoneNumber": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'PhoneNumber',
                'name': 'PhoneNumber',
                'placeholder': 'Phone Number',
                'required': True
            }), 
            "Achievements1": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach1',
                'name': 'ach1',
                'placeholder': '1.)',
                'required': False
            }), 
            "Achievements2": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach2',
                'name': 'ach2',
                'placeholder': '2.)',
                'required': False
            }), 
            "Achievements3": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach3',
                'name': 'ach3',
                'placeholder': '3.)',
                'required': False
            }), 
            "Achievements4": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach4',
                'name': 'ach4',
                'placeholder': '4.)',
                'required': False
            }), 
            "Achievements5": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach5',
                'name': 'ach5',
                'placeholder': '5.)',
                'required': False
            }), 
            "Achievements6": forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'ach6',
                'name': 'ach6',
                'placeholder': '6.)',
                'required': False
            })
        }