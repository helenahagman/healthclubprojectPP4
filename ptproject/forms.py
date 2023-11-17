from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Booking, Profile


class RegistrationForm(UserCreationForm):
    
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            auth_user =authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['passord1'],
            )
            login(self.request, auth_user)
        
        return user


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
