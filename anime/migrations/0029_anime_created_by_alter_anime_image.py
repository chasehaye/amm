# Generated by Django 5.0.6 on 2024-12-17 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0028_alter_anime_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_animes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='anime_images/'),
        ),
    ]
