# Generated by Django 5.0.6 on 2024-10-16 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0020_remove_studio_studioname_anime_studio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='type',
            field=models.CharField(choices=[('TV', 'TV'), ('Movie', 'Movie')], default='TV', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studio',
            name='website',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
