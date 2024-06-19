from django.db import models

# Create your models here.
class Media(models.Model):
    name = models.CharField(max_length=8, default='', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)