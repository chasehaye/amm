from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from anime.models import Anime

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    is_admin = models.BooleanField(default=False)



    currently_watching = models.ManyToManyField(Anime, related_name='currently_watched_by', blank=True)
    completed = models.ManyToManyField(Anime, related_name='completed_by', blank=True)
    plan_to_watch = models.ManyToManyField(Anime, related_name='planned_to_watch_by', blank=True)
    dropped = models.ManyToManyField(Anime, related_name='dropped_by', blank=True)
    interested_in = models.ManyToManyField(Anime, related_name='interested_by', blank=True)
    on_hold = models.ManyToManyField(Anime, related_name='on_hold_by', blank=True)












    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()