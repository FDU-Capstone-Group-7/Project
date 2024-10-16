from django.contrib import admin
from .model.game import Game 
from Indie_Game.model.Discussion import Discussion, Comment
# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'genre', 'stage', 'video_link', 'description']

# Customize the display of the Discussion model in the admin
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'game', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'game')
    search_fields = ('title', 'content', 'author__username', 'game__title')

# Customize the display of the Comment model in the admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'discussion', 'created_at')
    list_filter = ('created_at', 'discussion')
    search_fields = ('author__username', 'discussion__title', 'content')

# Register your models
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment, CommentAdmin)