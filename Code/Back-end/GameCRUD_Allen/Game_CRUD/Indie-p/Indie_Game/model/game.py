from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    releaseDate = models.DateField(blank=True, null=True)
    homepageURL =  models.URLField(blank = True)
    image = ImageField(upload_to='game_images/', blank=True, null=True)

    def __str__(self):
        return self.title