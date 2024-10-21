from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Indie_Game.model.game import Game


class Discussion(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='discussions')
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Indie_Game_comment'
        
    def __str__(self):
        return f'Comment by {self.author} on {self.discussion}'

class Comment_temp(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='temp_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Indie_Game_comment_temp'