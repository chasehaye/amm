from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from anime.models import Anime
from django.conf import settings
from django.core.exceptions import ValidationError

class WatchedEpisodes(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watched_episodes')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='watched_episodes')
    episodes_watched = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ['user', 'anime']

    def save(self, *args, **kwargs):
        print(self.episodes_watched)
        if self.episodes_watched is None:
            pass
        elif self.episodes_watched < 0:
            self.episodes_watched = None
        elif self.anime.episodes is not None and self.episodes_watched > self.anime.episodes:
            self.episodes_watched = self.anime.episodes

        super().save(*args, **kwargs)

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    is_admin = models.BooleanField(default=False)




    currently_watching = models.ManyToManyField(Anime, related_name='currently_watching', blank=True)
    completed = models.ManyToManyField(Anime, related_name='completed', blank=True)
    plan_to_watch = models.ManyToManyField(Anime, related_name='planned_to_watch', blank=True)
    dropped = models.ManyToManyField(Anime, related_name='dropped', blank=True)
    interested_in = models.ManyToManyField(Anime, related_name='interested_in', blank=True)
    on_hold = models.ManyToManyField(Anime, related_name='on_hold', blank=True)












    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()