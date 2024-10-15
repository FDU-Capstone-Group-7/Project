from django.contrib import admin
from .model.game import Game 
# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'genre', 'stage', 'video_link', 'description']

