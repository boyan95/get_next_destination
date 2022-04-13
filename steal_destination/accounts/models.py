from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from steal_destination.accounts.managers import TravellerUsersManager
from steal_destination.common.validators import only_letters_validator


class TravellerUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'

    objects = TravellerUsersManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    # DEFAULT_CHOOSE_FIELD = '--------'

    # MALE = 'Male'
    # FEMALE = 'Female'
    # DO_NOT_SHOW = 'Do not show'
    #
    # GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    image = models.ImageField()
    user = models.OneToOneField(
        TravellerUser,
        on_delete=models.CASCADE,
        primary_key=True,

    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
