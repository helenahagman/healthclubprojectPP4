from django.core.mail import send_mail
from django.views import generic, View
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from .models import BookingRequest, Profile, Contact
from .forms import RegistrationForm, ContactForm, BookingRequestForm


def index(request):
    """
    Renders the home view.
    """
    return render(request, 'index.html')


class PersonalTrainer(generic.View):
    """
    Implementation for the PersonalTrainer view
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'personaltrainer.html')


class MemberView(View):
    """
    Implementation for the Member view
    """
    template_name = 'member.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)



def book_request_view(request):
    """
    To render the booking request view.
    """
    return render(request, 'personaltrainer.html')


def register(request):
    """
    To render the registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'register.html', context)


def log_in(request):
    """
    To log in the user and redirect to the profile page
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Profile')
    else:
        form = AuthenticationForm()
    
    context = {
        'title': 'Login',
        'form' : form,
    }
    return render(request, 'login.html', context)


def log_out(request):
    """
    To log out the user and redirect to start page
    """
    logout(request)
    return redirect('index')
 

class Profile(generic.View):
    """
    Implementation for the User profile view
    """
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name_contact = form.cleaned_data['name_contact']
            email = form.cleaned_data['email']
            contact_message = form.cleaned_data['contact_message']
            
            from_email = settings.DEFAULT_FROM_EMAIL
            
            messages.success(request, 'Your message has been sent.')
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
