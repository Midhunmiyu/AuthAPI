
from django.urls import path
from account.views import UserPasswordResetView, UserProfileView, UserRegistrationView,UserLoginView, UserchangePasswordView,SendPasswordResetEmailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('changepassword/', UserchangePasswordView.as_view(),name='changepassword'),
    path('sent-reset-password-email/', SendPasswordResetEmailView.as_view(),name='sent-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),name='reset-password'),

]