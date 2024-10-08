# Generated by Django 5.0.6 on 2024-10-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_anime_episodeduration_anime_episodes_season_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi')], default='Horror', max_length=20),
            preserve_default=False,
        ),
    ]
