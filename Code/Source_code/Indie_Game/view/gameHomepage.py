from django.shortcuts import render, get_object_or_404
from ..model.homepage import Homepage

def game_homepage(request, slug):
    homepage = get_object_or_404(Homepage, slug=slug) 
    genres = homepage.game.genre.split(', ') if homepage.game.genre else [] 

    stage_values = {
        'CONCEPT': 10,
        'PRE-PRODUCTION': 20,
        'DEVELOPMENT': 50,
        'ALPHA': 60,
        'BETA': 80,
        'RELEASED': 100,
        'POST-RELEASE': 100
    }

    bg_values = {
        'CONCEPT': 'bg-danger',
        'PRE-PRODUCTION': 'bg-secondary',
        'DEVELOPMENT': 'bg-warning',
        'ALPHA': 'bg-primary',
        'BETA': 'bg-info',
        'RELEASED': 'bg-success',
        'POST-RELEASE': 'bg-success'

    }
    stage = homepage.game.stage
    progress_value = stage_values.get(stage, 0)
    bar_color = bg_values.get(stage,'bg-primary')


    return render(request, 'game/gameHomepage.html', {'game': homepage.game, 'homepage': homepage,'genres': genres,'progress_value': progress_value,'bar_color':bar_color})
