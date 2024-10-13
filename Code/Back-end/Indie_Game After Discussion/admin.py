from django.contrib import admin
from .model.game import Game 
from .model.discussion import Discussion
from .model.discussion import Comment

# Register your models here.
@admin.register(Game)
class UserAdmin(admin.ModelAdmin):
    list_display=('title','description','releaseDate','homepageURL','image')

@admin.register(Discussion)
class UserAdmin(admin.ModelAdmin):
    list_display=('game','title','content','author','created_at','updated_at')

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display=('discussion','author','content','created_at')