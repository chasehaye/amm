from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from anime.models import Anime

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    is_admin = models.BooleanField(default=False)






# unfinihsed
    currently_watching = models.ManyToManyField(Anime, related_name='currently_watching', blank=True)
    completed = models.ManyToManyField(Anime, related_name='completed', blank=True)
    plan_to_watch = models.ManyToManyField(Anime, related_name='planned_to_watch', blank=True)
    dropped = models.ManyToManyField(Anime, related_name='dropped', blank=True)
    interested_in = models.ManyToManyField(Anime, related_name='interested_in', blank=True)
    on_hold = models.ManyToManyField(Anime, related_name='on_hold', blank=True)












    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()