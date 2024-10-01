# Contributor: Dmitriy Sizionov
# Date: 01-oct-2024
# Class for creation a game page

from django.db import models

class Game(models.Model):
    gameID = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    releaseDate = models.DateField()
    homepageURL =  models.URLField(blank = True)
