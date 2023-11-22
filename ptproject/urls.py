from . import views
from django.urls import path
from .views import (
    register,
    MemberView,
    contact,
    log_in,
    log_out,
    ProfileView,
    PersonalTrainerView,
    BookView,
    membersonlyView,
    EditProfileView,
    CustomSignupView,
)


urlpatterns = [
    path("", views.index, name="index"),
    path("personaltrainer/", PersonalTrainerView.as_view(), name='personaltrainer'),
    path("member/", MemberView.as_view(), name="member"),
    path("book/", BookView.as_view(), name="booking"),
    path("accounts/register/", register, name="account_signup"),
    path("accounts/signup/", CustomSignupView.as_view(), name="custom_signup"),
    path("accounts/login/", log_in, name='login'),
    path("profile/", ProfileView.as_view(), name="profile_view"),
    path("contact/", contact, name="contact"),
    path("logout/", log_out, name='logout'),
    path("membersonly/", membersonlyView.as_view(), name="membersonly"),
    path("profile/edit/", EditProfileView.as_view(), name="edit_profile"),
]