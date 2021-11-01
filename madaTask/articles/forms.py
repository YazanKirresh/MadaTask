from django import forms
from django.forms.models import ModelForm
from .models import Customer,Service

class customerRegistrationForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'




class serviceRegistration(forms.Form):
   class Meta:
        model = Service
        fields = '__all__' 
        