# Generated by Django 5.0.6 on 2024-12-15 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_watchedepisodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchedepisodes',
            name='episodes_watched',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]