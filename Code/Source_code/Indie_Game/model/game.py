from django.db import models
from .userprofile import UserProfile
from django.utils.text import slugify

class Game(models.Model):
    title = models.CharField(max_length=100,default="unspecified")
    publisher = models.CharField(max_length=100,default="unspecified")
    genre = models.CharField(max_length=200,default="unspecified")
    stage = models.CharField(max_length=50,default="unspecified")
    cover_image = models.ImageField(upload_to='cover_images/',default='default.jpg')
    video_link = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(default="not provided")
    short_intro = models.TextField(default="not provided")
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default=1,related_name='games') 
    slug = models.SlugField(max_length=200, unique=True, blank=True) 
    game_rating = models.FloatField(default=5)


    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super(Game, self).save(*args, **kwargs)



    def __str__(self):
        return self.title
        