from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .model.game import Game
from .model.update import Update  
from .model.homepage import Homepage  

def is_owner(view_func):
    def wrapper(request, *args, **kwargs):

        if 'update_id' in kwargs: #updates CRUD

            update_instance = get_object_or_404(Update, pk=kwargs['update_id'])
  
            homepage = update_instance.homepage
            game = homepage.game

        elif 'slug' in kwargs: #add_update
            homepage = get_object_or_404(Homepage, slug=kwargs['slug'])
            game = homepage.game

        elif 'id' in kwargs: #game CRUD

            game = get_object_or_404(Game, pk=kwargs['id'])
        else:

            return HttpResponseForbidden("Invalid request parameters.")
        

        if game.owner != request.user.userprofile:
            return HttpResponseForbidden("You are not allowed to access this resource.")

        return view_func(request, *args, **kwargs)

    return wrapper
