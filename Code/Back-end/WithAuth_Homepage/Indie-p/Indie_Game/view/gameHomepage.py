from django.shortcuts import render, get_object_or_404
from ..model.homepage import Homepage

def game_homepage(request, slug):
    homepage = get_object_or_404(Homepage, slug=slug) 
    return render(request, 'game/gameHomepage.html', {'game': homepage.game, 'homepage': homepage})
