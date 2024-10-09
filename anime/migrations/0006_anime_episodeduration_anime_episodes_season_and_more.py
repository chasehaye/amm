# Generated by Django 5.0.6 on 2024-10-09 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_rename_titlejpkanj_anime_titlejpkanji'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='episodeDuration',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('season', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')], max_length=20)),
            ],
            options={
                'ordering': ['-year', 'season'],
                'unique_together': {('year', 'season')},
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='premiereSeason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='anime.season'),
        ),
    ]
