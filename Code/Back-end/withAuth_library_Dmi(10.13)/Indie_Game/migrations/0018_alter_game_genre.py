# Generated by Django 5.1.1 on 2024-10-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indie_Game', '0017_remove_game_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(default='unspecified', max_length=200),
        ),
    ]
