# Generated by Django 5.0.6 on 2024-10-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0009_alter_anime_prequel_alter_anime_sequel'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='demographic',
            field=models.CharField(choices=[('Shonen', 'Shonen'), ('Seinen', 'Seinen'), ('Shojo', 'Shojo')], default='Shojo', max_length=20),
            preserve_default=False,
        ),
    ]
