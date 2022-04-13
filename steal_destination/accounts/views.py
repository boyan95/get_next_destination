from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import PasswordChangeForm

from steal_destination.accounts.forms import UserRegistrationForm, EditProfileForm
from steal_destination.accounts.models import Profile, TravellerUser
from django.urls import reverse_lazy
from django.views import generic as views

UserModel = get_user_model


# премахвам за момент RedirectToIndex от UserRegisterView
class UserRegisterView(views.CreateView):
    model = Profile
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    # регистриране и логване след това
    def form_valid(self, form):
        result = super().form_valid(form)
        # user = self.object
        # request = self.request
        login(self.request, self.object)
        return result

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #
    #     kwargs['user'] = self.request.user
    #     return kwargs


class ProfileView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


class UserLoginView(auth_views.LoginView):
    form_class = auth_forms.AuthenticationForm
    template_name = 'accounts/login_page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.pk,))


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    model = Profile
    form_class = PasswordChangeForm
    template_name = 'accounts/change_password.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.request.user.pk,))


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'accounts/profile_delete.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('index')
