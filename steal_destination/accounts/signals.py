from django.contrib.auth import get_user_model

from django.db.models import signals
from django.dispatch import receiver
from .models import Profile, TravellerUser
from .views import DeleteProfileView
from ..main.models import Destination, Blog


@receiver(signals.post_save, sender=TravellerUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile was created')


@receiver(signals.post_save, sender=TravellerUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print('profile was saved')


# def delete_user(sender,instance)

@receiver(signals.post_save, sender=Destination)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.save()
    print(f'Destination: {instance} was created')


# def delete_user(sender,instance)
@receiver(signals.post_delete, sender=Profile)
def delete_user(sender, instance, using, **kwargs):
    user = TravellerUser.objects.get(pk=instance.user.id)
    user.delete()
    print(f'user wad deleted')


@receiver(signals.pre_delete, sender=Profile)
def delete_all_additional_information(sender, instance, using, **kwargs):
    destinations = Destination.objects.filter(user_id=instance.pk)
    articles = Blog.objects.filter(user_id=instance.pk)
    # user = TravellerUser.objects.get(pk=instance.pk)
    if destinations:
        destinations.delete()
    if articles:
        articles.delete()
    # user.delete()
    print(f'all information about {instance} were deleted')
