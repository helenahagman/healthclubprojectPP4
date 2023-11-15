from django.contrib import admin
from .models import BookingRequest, UserProfile, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BookingRequest)
class BookingRequestAdmin(SummernoteModelAdmin):
    list_display = ('name', 'phonenumber', 'email', 'age', 'gender', 'message', 'date', 'time', 'get_approved')
    search_fields = ('name', 'get_approved')
    list_filter = ('name',)

    actions = ['approve_booking', 'unapprove_booking']

    def get_approved(self, obj):
        return obj.approved
    get_approved.short_description = 'Request Approved'

    def unapprove_booking(self, request, queryset):
        queryset.update(approved='not_approved')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_contact', 'email', 'contact_message', 'created_on')
    list_filter = ('name_contact', 'email', 'created_on',)
    list_display_links = ('name_contact',)
    search_fields = ['name_contact', 'email', 'contact_message', 'created_on']

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'email', )
    list_filter = ('user',)
    search_fields = ('user', 'first_name', 'last_name', 'phone_number', 'email',)
