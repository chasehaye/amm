# Generated by Django 5.0.6 on 2024-10-09 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_anime_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='prequel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sequel_anime', to='anime.anime'),
        ),
        migrations.AddField(
            model_name='anime',
            name='sequel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prequel_anime', to='anime.anime'),
        ),
    ]
