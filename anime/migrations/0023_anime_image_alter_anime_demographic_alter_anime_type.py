# Generated by Django 5.0.6 on 2024-11-15 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0022_anime_created_at_anime_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='anime_images/'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='demographic',
            field=models.CharField(choices=[('Shounen', 'Shounen'), ('Seinen', 'Seinen'), ('Shoujo', 'Shoujo'), ('Josei', 'Josei')], max_length=20),
        ),
        migrations.AlterField(
            model_name='anime',
            name='type',
            field=models.CharField(choices=[('TV', 'TV'), ('Movie', 'Movie'), ('OVA', 'OVA')], max_length=20),
        ),
    ]