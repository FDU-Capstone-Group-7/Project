
from django.db import models
from ..model.game import Game

class Picture(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_pictures')
    image = models.ImageField(upload_to='game_pictures/')