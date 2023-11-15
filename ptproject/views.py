from django.shortcuts import render
from django.views import generic
from .models import BookingRequest, UserProfile, Contact


def home(request):
    """
    Renders the home view.
    """
    return render(request, 'index.html')


def sign_in(request):
    """
    To render the sign in view.
    """
    return render(request, 'sign_in.html')


def register(request):
    """
    To render the registration view.
    """
    return render(request, 'register.html')





