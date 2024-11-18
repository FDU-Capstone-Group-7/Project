from django.db import models
from .userprofile import UserProfile
from .update import Update
from .homepage import Homepage

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')
    update = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='ratings')
    homepage = models.ForeignKey(Homepage, on_delete=models.CASCADE, related_name='ratings')  
    score = models.FloatField()


    class Meta:
        unique_together = ('user', 'update')   

def __str__(self):
        return f"Rating {self.score} by {self.user} for {self.update.update_title}"
