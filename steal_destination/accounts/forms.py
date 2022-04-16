from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.core.validators import MinLengthValidator
from steal_destination.accounts.models import Profile
from steal_destination.common.validators import only_letters_validator
from steal_destination.main.models import Destination

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2', 'first_name', 'last_name']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            image=self.cleaned_data['image'],
            user=user)
        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'image')

        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter email",
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter password",
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter password again",

                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter first name",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter last name",
                }
            ),
            'image': forms.ImageField(),

        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter first name",
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter last name",
                }),
        }



