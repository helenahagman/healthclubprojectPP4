from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Contact, Booking, Profile, Session


class ContactForm(forms.Form):
    name_contact = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact_message = forms.CharField(widget=forms.Textarea)
            
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)


class BookingForm(forms.ModelForm):
     # session = forms.ModelChoiceField(queryset=Session.objects.all(), empty_label="Select a session", label="Session")

    class Meta:
        model = Booking
        fields = ['session', 'name', 'phonenumber', 'email', 'age', 'gender', 'message']
                
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


# class CustomSignupForm(SignupForm):
#     phone_number = forms.CharField(max_length=15)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required information')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
