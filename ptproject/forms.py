from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Contact, Booking, Profile


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name_contact', 'email', 'contact_message']
        labels = {
            'name_contact': 'Your name',
            'email': 'Email',
            'contact_message': 'Message',
        }
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


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
            'name': forms.TextInput(attrs={'placeholder': 'State your name'}),
            'phonenumber': forms.TextInput(attrs={'placeholder': '1234567890'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@mail.com'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'placeholder': 'Select your gender'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select a date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'Select a time'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
