from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, ValidationError
from ptproject.utils import num_validation, alpha_only


STATUS = ((0, "Draft"), (1, "Published"))




class Booking(models.Model):
    """
    Create a booking request form
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, default='State your name')
    phonenumber = models.CharField(max_length=15, default='1234567890')
    email = models.EmailField(max_length=70, default='your@mail.com')
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        default='male'
    )
    message = models.TextField(max_length=300, default='')
    date = models.DateField()
    time = models.TimeField()
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Booking by {self.name} on {self.date} at {self.time}'

class Contact(models.Model):
    """
    Model for contact messages.

    """

    name_contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, default='default@example.com')
    contact_message = models.TextField(max_length=400, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'Contact message submitted by {self.name_contact} on {self.created_on}'


class Profile(models.Model):
    """
    User profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=70, default='default@example.com')
    phone_number = models.CharField(max_length=50, null=True, blank=True, validators=[num_validation])
    first_name = models.CharField(max_length=50, null=True, blank=True, validators=[alpha_only])
    last_name = models.CharField(max_length=50, null=True, blank=True, validators=[alpha_only])
    password = models.CharField(max_length=128, null=True, blank=True)


    def __str__(self):
        return f'{self.user} profile'