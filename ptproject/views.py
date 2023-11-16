from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from .models import BookingRequest, UserProfile, Contact


def index(request):
    """
    Renders the home view.
    """
    return render(request, 'index.html')


class PersonalTrainer(generic.View):
    """
    Implementation for the PersonalTrainer view
    """


class Member(generic.View):
    """
    Implementation for the Member view
    """


def book_request_view(request):
    """
    To render the booking request view.
    """
    return render(request, 'personaltrainer.html')


def sign_in(request):
    """
    To render the sign in view.
    """
    return render(request, 'sign_in.html')


class Register(generic.View):
    """
    To render the registration view.
    """

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
