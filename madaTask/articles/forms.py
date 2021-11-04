from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Service


class customer_registration_form(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class service_registration_form(ModelForm):
   class Meta:
        model = Service
        fields = '__all__' 


class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']