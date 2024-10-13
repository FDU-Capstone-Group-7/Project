from django.contrib import admin
from .model.game import Game 
# Register your models here.
@admin.register(Game)
class UserAdmin(admin.ModelAdmin):
    list_display=('title','description','releaseDate','homepageURL','image')
