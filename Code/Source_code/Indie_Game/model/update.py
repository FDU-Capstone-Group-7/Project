from django.db import models
from .homepage import Homepage

class Update(models.Model):
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='updates')
    update_title = models.CharField(max_length=100,default="unspecified")
    update_date = models.DateField()
    patch_notes = models.TextField()
    downloadable = models.URLField(max_length=500, blank=True, null=True)
    video = models.URLField(max_length=500, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    


    def __str__(self):
        return f"Update on {self.update_date} for {self.game.title}"
