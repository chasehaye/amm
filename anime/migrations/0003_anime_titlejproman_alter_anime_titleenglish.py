# Generated by Django 5.0.6 on 2024-10-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_remove_anime_airdate_remove_anime_animetype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='titleJpRoman',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='titleEnglish',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
