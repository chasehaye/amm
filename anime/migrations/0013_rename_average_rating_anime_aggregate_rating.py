# Generated by Django 5.0.6 on 2024-10-09 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_anime_average_rating_anime_rating_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='average_rating',
            new_name='aggregate_rating',
        ),
    ]