from django import forms
from .models import Logger

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 

#MODEL-FORM (must register in admin)
class ModelForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'  #import all firls from logger for modelform