from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (   
        ('dev', 'Developer'),
        ('player', 'Player'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True,null=True) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    account_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username
