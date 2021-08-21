from django.forms import ModelForm
from .models import Customer
from django import forms

class CustomerForm(ModelForm):
   class Meta:
         model = Customer
         fields = '__all__'
         widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }