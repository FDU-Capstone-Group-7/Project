# Generated by Django 5.1.1 on 2024-09-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indie_Game', '0003_alter_game_description_alter_game_releasedate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gameID',
        ),
        migrations.AddField(
            model_name='game',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
