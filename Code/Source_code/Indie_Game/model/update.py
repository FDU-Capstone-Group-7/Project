from django.db import models
from .homepage import Homepage
from .game import Game

class Update(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,related_name='updates')
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='updates')
    update_title = models.CharField(max_length=100)
    update_date = models.DateField()
    patch_notes = models.TextField()
    downloadable = models.URLField(max_length=500, blank=True, null=True)
    video = models.URLField(max_length=500, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)

    
    def __str__(self):
             return f"Update on {self.update_date} for {self.game.title}"
    
