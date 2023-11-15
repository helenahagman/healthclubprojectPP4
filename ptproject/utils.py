import random
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms


def num_validation(num):
    if not num. isdigit():
        raise ValidationError('Only numbers are allowed in this feild')


def name_validation(name):
    name = ['username', 'first_name', 'last_name', 'name']
    if not name.isalpha():
        raise forms.ValidationError('Only letters are allowed in this feild')


def date_validation(date):
    if date < timezone.now().date():
        raise forms.ValidationError('You can only choose dates in the future')