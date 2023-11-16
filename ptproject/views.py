from django.core.mail import send_mail
from django.views import generic, View
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import BookingRequest, UserProfile, Contact
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
            return redirect('index')
    else:
        form = RegistrationForm()
    
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'register.html', context)


def log_in(request):
    """
    To render the login in view.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    context = {
        'title': 'Login',
        'form' : form,
    }
    return render(request, 'login.html', context)


class UserProfile(generic.View):
    """
    Implementation for the User profile view
    """
    template_name = 'userprofile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            subject = 'Contact Form Submission'
            message = 'Thank you, we will get back to you shortly!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['health.club.project.email@gmail.com']

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {'title': 'Contact', 'form' : form}
    return render(request, 'contact.html', context)
