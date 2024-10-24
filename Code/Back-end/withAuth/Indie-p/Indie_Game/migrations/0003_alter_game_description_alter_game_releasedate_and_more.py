# Generated by Django 5.1.1 on 2024-09-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indie_Game', '0002_game_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='releaseDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
