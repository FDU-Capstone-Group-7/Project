from django.db import models
from .userprofile import UserProfile
from .game import Game
from django.utils.text import slugify

class Homepage(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='homepages')
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='homepage')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.user.user.username}-{self.game.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Homepage for {self.game.title}"

