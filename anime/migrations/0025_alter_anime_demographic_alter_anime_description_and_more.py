# Generated by Django 5.0.6 on 2024-12-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0024_alter_anime_episodes_alter_anime_titleenglish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='demographic',
            field=models.CharField(choices=[('Shounen', 'Shounen'), ('Seinen', 'Seinen'), ('Shoujo', 'Shoujo'), ('Josei', 'Josei')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.CharField(max_length=1000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='episodeDuration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='type',
            field=models.CharField(choices=[('TV', 'TV'), ('Movie', 'Movie'), ('OVA', 'OVA')], null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
