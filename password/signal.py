from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django .dispatch import receiver
from .models import Profile

receiver(post_save,sender=User)
def create_profile_model(sender, instance, created, **kwargs):
    
    if created:
        profile=Profile.objects.create(User=instance)
        profile.save()