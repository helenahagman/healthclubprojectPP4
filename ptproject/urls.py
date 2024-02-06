from . import views
from django.urls import path
from django.contrib.auth.views import LoginView
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
    sessions_calendar,
    sessions_api
)


urlpatterns = [
    path("", views.index, name="index"),
    path('personaltrainer/', views.personal_trainer, name='personaltrainer'),
    path('member/', views.members, name='member'),
    path("book/", BookView.as_view(), name="booking"),
    path("accounts/register/", register, name="account_signup"),
    # path("accounts/signup/", CustomSignupView.as_view(), name="custom_account_signup"),
    # path("accounts/login/", log_in, name='login'),
    path("profile/", ProfileView.as_view(), name="profile_view"),
    path("contact/", views.contact_view, name="contact"),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path("logout/", log_out, name='logout'),
    path("membersonly/", membersonlyView.as_view(), name="membersonly"),
    path("profile/edit/", EditProfileView.as_view(), name="edit_profile"),
    path('sessions/calendar/', sessions_calendar, name='sessions_calendar'),
    path('api/sessions/', sessions_api, name='sessions_api'),
]