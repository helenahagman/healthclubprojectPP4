from . import views
from django.urls import path
from .views import register, MemberView, contact, log_in, log_out, Profile


urlpatterns = [
    path("", views.index, name="index"),
    path("personaltrainer/", views.PersonalTrainer.as_view(), name='personaltrainer'),
    path("member/", MemberView.as_view(), name="member"),
    path("book/", views.book_request_view, name="book"),
    path("register/", register, name="register"),
    path("login/", log_in, name='login'),
    path("profile/", Profile.as_view(), name="profile"),
    path("contact/", contact, name="contact"),
    path("logout/", log_out, name='logout'),
]