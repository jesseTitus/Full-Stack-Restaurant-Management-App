from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 

#MODEL-FORM (must register in admin)
class ModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'  #import all fields from model for modelform

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]