from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Contact, Booking, Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']
    
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.set_password(self.cleaned_data['password1'])
            user.save()

            profile = Profile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
            
            auth_user = authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1'],
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
