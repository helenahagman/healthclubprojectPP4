from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, BookingRequest


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name_contact', 'email', 'contact_message']


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['name', 'phonenumber', 'email', 'age', 'gender', 'message', 'date', 'time']
    
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
    }
