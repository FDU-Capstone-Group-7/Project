# Generated by Django 5.1.1 on 2024-09-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indie_Game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('gameID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('releaseDate', models.DateField()),
                ('homepageURL', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='game_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
