from . import views
from django.urls import urls


urlpatterns = [
    path("", views.home_view, name="index"),
    path(
        "personaltrainer/",
        views.PersonalTrainer.as_view(),
        name='personaltrainer'
    ),
    path("member/", views.Member.as_view(), name="member"),
    path("booking/", views.book_request_view, name="book_session"),
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.log_in, name='login'),
    path("userprofile/", views.UserProfile.as_view(), name="userprofile"),
    path("book/", views.Book.as_view(), name='book'),
]