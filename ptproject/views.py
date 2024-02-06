from django import forms
from django.urls import reverse
from django.core.mail import send_mail
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .models import Profile, Contact, Session
from .forms import ContactForm, BookingForm, ProfileForm, SignUpForm


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

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # check if the user is authenticated
        user = request.user
        if user.is_authenticated:
            # If authenticated, pre-fill form with user information
            profile = Profile.objects.get_or_create(user=user) [0]
            initial_data = {
                'name': user.get_full_name(),
                'email': user.email,
            }
            form = BookingForm(initial=initial_data)
        else:
            form = BookingForm()

        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the Booking model
            booking_instance = form.save(commit=False)
            booking_instance.approved = False
            booking_instance.user = request.user 
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
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        bookings = Booking.objects.filter(user=user)

        context = {
            'user': user,
            'profile': profile,
            'bookings': bookings,
        }
        
        return render(request, self.template_name, context)
    
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'edit_profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        form = ProfileForm(instance=profile)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile_view')
        return render(request, self.template_name, {'form': form})


# class CustomSignupForm(SignupForm):
#     phone_number = forms.CharField(max_length=15)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('profile')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class CustomSignupView(SignupView):
    template_name = 'account/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Register now'
        context['subheading'] = 'Make smart choices and live a healthier life.'
        return context
        
def register(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membersonly')
    else:
        form = CustomSignupForm()

    return render(request, 'signup.html', {'form': form})


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

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.save()

            name_contact = form.cleaned_data['name_contact']
            email = form.cleaned_data['email']
            contact_message = form.cleaned_data['contact_message']
            
            messages.success(request, 'Your message has been sent.')
            return HttpResponseRedirect('/success/')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


@login_required
def book_session(request, session_id):
    session = get_object_or_404(Session, id=session_id, booked=False)
    session.booked = True
    session.client = request.user
    session.save()
    return redirect('sessions_calendar')

def sessions_calendar(request):
    return render(request, 'sessions_calendar.html')

def sessions_api(request):
    sessions = Session.objects.filter(booked=False)
    session_data = [{
        'title': f"Session with {session.trainer.username}",
        'start': f"{session.date}T{session.start_time}",
        'end': f"{session.date}T{session.end_time}",
        'url': f"/book/{session.id}/",
    } for session in sessions]
    return JsonResponse(session_data, safe=False)


def personal_trainer(request):
    context = {
        'header': 'Personal Trainer',
        'subheading': 'A session with a Personal Trainer can make the whole difference.',
    }
    return render(request, 'personaltrainer.html', context)

def members(request):
    context = {
        'header': 'Members',
        'subheading': 'As a member you get access to all the best offers and news!',
    }
    return render(request, 'member.html', context)

def login(request):
    context = {
        'header': 'Stay active',
        'subheading': 'Daily exercise helps you to stay strong and healthy.',
    }
    return render(request, 'login.html', context)

def signup(request):
    context = {
        'header': 'Welcome',
        'subheading': 'Make smart choices and live a healthier life.',
    }
    return render(request, 'signup.html', context)

def contact(request):
    context = {
        'header': 'Contact us',
        'subheading': 'We are here for you, fill in the form and let us know whats on your mind',
    }
    return render(request, 'contact.html', context)

def book(request):
    context = {
        'header': 'Book PT session',
        'subheading': 'A session with an expert will get you started, no matter what your goal is! ',
    }
    return render(request, 'book.html', context)