from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary import models as clodinary_models
from steal_destination.common.validators import validate_file_max_size_in_mb

UserModel = get_user_model()


class Destination(models.Model):
    COUNTRY_NAME_MAX_LENGTH = 50
    VENUE_NAME_MAX_LENGTH = 50

    INTERNATIONAL_VACATION = 'International vacation'
    DOMESTIC_VACATION = 'Domestic vacation'
    CITY_VACATION = 'City vacation'
    CAMPING_VACATION = 'Camping vacation'
    RESORT_VACATION = 'Resort vacation'
    CRUISE_VACATION = 'Cruise vacation'
    SOLO_VACATION = 'Solo vacation'

    TYPES = [(x, x) for x in (
        INTERNATIONAL_VACATION,
        DOMESTIC_VACATION,
        CITY_VACATION,
        CAMPING_VACATION,
        RESORT_VACATION,
        CRUISE_VACATION,
        SOLO_VACATION)
             ]

    # fields(columns)
    country_name = models.CharField(
        max_length=COUNTRY_NAME_MAX_LENGTH,
    )
    venue_name = models.CharField(
        max_length=VENUE_NAME_MAX_LENGTH,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    date_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = clodinary_models.CloudinaryField('image')
    likes = models.ManyToManyField(UserModel, related_name='destination_likes')

    # one-to-one

    # one-to-many
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return f'{self.user} {self.country_name}, {self.venue_name}'

    def total_likes(self):
        return self.likes.count()


# many-to-many
# properties

# methods

# dunder methods
# Meta


class Blog(models.Model):
    MAX_ARTICLE_NAME = 50
    MIN_ARTICLE_NAME = 3

    article_name = models.CharField(
        max_length=MAX_ARTICLE_NAME,
    )
    description = models.TextField()
    image = clodinary_models.CloudinaryField('image')
    likes = models.ManyToManyField(
        UserModel, related_name='blog_likes'
    )
    # one-to-many
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.article_name

    def total_likes(self):
        return self.likes.count()


class Post(models.Model):
    COUNTRY_NAME_MAX_LENGTH = 50
    VENUE_NAME_MAX_LENGTH = 50

    country_name = models.CharField(max_length=COUNTRY_NAME_MAX_LENGTH)
    venue_name = models.CharField(max_length=VENUE_NAME_MAX_LENGTH)
    description = models.TextField()
    image = clodinary_models.CloudinaryField('image')

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.country_name


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = clodinary_models.CloudinaryField('image')

    def __str__(self):
        return self.post.country_name
