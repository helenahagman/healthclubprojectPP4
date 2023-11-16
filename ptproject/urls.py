from . import views
from django.urls import path
from .views import register, MemberView, contact


urlpatterns = [
    path("", views.index, name="index"),
    path("personaltrainer/", views.PersonalTrainer.as_view(), name='personaltrainer'),
    path("member/", MemberView.as_view(), name="member"),
    path("book/", views.book_request_view, name="book"),
    path("register/", register, name="register"),
    path("login/", views.log_in, name='login'),
    path("userprofile/", views.UserProfile.as_view(), name="userprofile"),
    path("contact/", contact, name="contact",)
]