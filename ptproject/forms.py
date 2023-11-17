from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Booking


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name_contact', 'email', 'contact_message']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phonenumber', 'email', 'age', 'gender', 'message', 'date', 'time']
        labels = {
            'name': 'Your Name',
            'phonenumber': 'Phone Number',
            'email': 'Email',
            'age': 'Age',
            'gender': 'Gender',
            'message': 'Message',
            'date': 'Preferred Date',
            'time': 'Preferred Time',
        }
        help_texts = {
            'date': 'Select a date.',
            'time': 'Select a time.',
        }
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
