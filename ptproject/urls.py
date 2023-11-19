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
)


urlpatterns = [
    path("", views.index, name="index"),
    path("personaltrainer/", PersonalTrainerView.as_view(), name='personaltrainer'),
    path("member/", MemberView.as_view(), name="member"),
    path("book/", BookView.as_view(), name="booking"),
    path("register/", register, name="register"),
    path("login/", log_in, name='login'),
    path("profile/", ProfileView.as_view(), name="profile_view"),
    path("contact/", contact, name="contact"),
    path("logout/", log_out, name='logout'),
    path("membersonly/", membersonlyView.as_view(), name="membersonly")
]