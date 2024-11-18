from django.db import models
from .update import Update


class UpdatePicture(models.Model):
    update = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='update_pictures')
    image = models.ImageField(upload_to='update_pictures/')
    image_caption = models.TextField(default="not provided")

