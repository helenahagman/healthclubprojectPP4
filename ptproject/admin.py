from django.contrib import admin
from .models import Profile, Contact, Session, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'phonenumber', 'email', 'age', 'gender', 'message', 'date', 'time', 'approved')
    search_fields = ('name', 'approved')
    list_filter = ('name', 'date')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)

    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_contact', 'email', 'contact_message', 'created_on')
    list_filter = ('name_contact', 'email', 'created_on',)
    list_display_links = ('name_contact',)
    search_fields = ['name_contact', 'email', 'contact_message', 'created_on']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'email', )
    list_filter = ('user',)
    search_fields = ('user', 'first_name', 'last_name', 'phone_number', 'email',)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['trainer_name', 'session_type', 'date', 'start_time', 'end_time',]
    list_filter = ['date', 'trainer_name']