# Generated by Django 5.0.6 on 2024-10-09 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0013_rename_average_rating_anime_aggregate_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='aggregate_rating',
            new_name='aggregateRating',
        ),
    ]