from django.urls import reverse
from django.core.mail import send_mail
from django.views import generic, View
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Booking, Profile, Contact
from .forms import RegistrationForm, ContactForm, BookingForm


def index(request):
    """
    Renders the home view.
    """
    return render(request, 'index.html')


class PersonalTrainerView(View):
    """
    Implementation for the PersonalTrainer view
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'personaltrainer.html')


class membersonlyView(View):
    """
    Implementation for the Membersonly view
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'membersonly.html')
        else:
            return redirect('login')


class BookView(View):
    """
    Implementation for the book view
    """
    template_name = 'book.html'

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the Booking model
            booking_instance = form.save(commit=False)
            booking_instance.approved = False
            booking_instance.save()

            name = form.cleaned_data['name']  
            phonenumber = form.cleaned_data['phonenumber']  
            email = form.cleaned_data['email']  
            age = form.cleaned_data['age']  
            gender = form.cleaned_data['gender']  
            message = form.cleaned_data['message']  
            date = form.cleaned_data['date']  
            time = form.cleaned_data['time']
            
            messages.success(request, 'Your request has been sent.')
            return HttpResponseRedirect(reverse('booking'))
        else:
            form = BookingForm()

        return render(request, 'book.html', {'form': form})


class MemberView(View):
    """
    Implementation for the Member view
    """
    template_name = 'member.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfileView(LoginRequiredMixin, View):
    """
    Implementation for the User profile view
    """
    template_name = 'profile_view.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.get(user=user)
        bookings = Booking.objects.filter(user=user)

        context = {
            'user': user,
            'profile': profile,
            'bookings': bookings,
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)



def register(request):
    """
    To render the registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            new_user = authenticate(
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password1')
            )

            login(request, new_user)

            return redirect ('index')

    else:
        form = RegistrationForm(request)
    
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'membersonly.html', context)

@csrf_protect
def log_in(request):
    """
    To log in the user and redirect to the profile page
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile_view')
    else:
        form = AuthenticationForm()
    
    context = {
        'title': 'Login',
        'form' : form,
    }
    return render(request, 'login.html', context)

@login_required
def log_out(request):
    """
    To log out the user and redirect to start page
    """
    logout(request)
    return redirect('index')
 


@login_required
def profile_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    bookings = Booking.objects.filter(user=user)

    context = {
        'user': user,
        'profile': profile,
        'bookings': bookings,
    }

    return render(request, 'profile.html', context)

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
