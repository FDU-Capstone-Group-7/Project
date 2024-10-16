# Generated by Django 5.1.1 on 2024-10-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Indie_Game', '0008_alter_userprofile_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='homepageURL',
        ),
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.RemoveField(
            model_name='game',
            name='releaseDate',
        ),
        migrations.AddField(
            model_name='game',
            name='cover_image',
            field=models.ImageField(default='default.jpg', upload_to='cover_images/'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(default='unspecified', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='game_pictures/'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.CharField(default='unspecified', max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='stage',
            field=models.CharField(default='unspecified', max_length=50),
        ),
        migrations.AddField(
            model_name='game',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(default='unspecified', max_length=100),
        ),
    ]