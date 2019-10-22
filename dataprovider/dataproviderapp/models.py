from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	is_online = models.BooleanField(default=False)
	

@receiver(user_logged_in, sender = User)
def user_profile_logged_in(sender, user, request, **kwargs):
	print("singal working")
	profile = UserProfile.objects.get(user = user)
	profile.is_online = "True"
	profile.save()


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user = instance)

@receiver(post_save, sender = User)		
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()