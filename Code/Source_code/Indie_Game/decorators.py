from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .model.game import Game
from .model.userprofile import UserProfile  

def is_owner(view_func):
    def wrapper(request, *args, **kwargs):
        game = get_object_or_404(Game, pk=kwargs['id']) 

        if game.owner != request.user.userprofile:
            return HttpResponseForbidden("You are not allowed to access this resource.")
        return view_func(request, *args, **kwargs)
    return wrapper
