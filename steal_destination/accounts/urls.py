from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

from steal_destination.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ChangeUserPasswordView, \
    ProfileView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
]
import steal_destination.accounts.signals
