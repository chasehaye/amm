# Generated by Django 5.0.6 on 2024-12-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0030_alter_anime_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='website',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
