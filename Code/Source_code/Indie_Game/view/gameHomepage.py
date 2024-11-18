from django.shortcuts import render, get_object_or_404
from ..model.homepage import Homepage
from ..model.update import Update
from ..model.rating import Rating

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages


def calculate_average_rating(game):
    valid_updates = game.updates.filter(average_rating__gt=0)  # filtering updates whoes score is none or zero
    total_score = sum(update.average_rating for update in valid_updates)
    total_updates = valid_updates.count()

    if total_updates > 0:
        return round(total_score / total_updates, 2)
    return 0.0  # no valid updates then return 0

# progress bar
def get_stage_info(stage):
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

    progress_value = stage_values.get(stage, 0)
    bar_color = bg_values.get(stage, 'bg-primary')
    return progress_value, bar_color

def get_rating_status(user, update_id):
    try:
        # 检查是否存在相应的 Rating 记录
        return Rating.objects.filter(user=user, update_id=update_id).exists()
    except Rating.DoesNotExist:
        return False


@login_required
def game_homepage(request, slug):
    homepage = get_object_or_404(Homepage, slug=slug)
    genres = homepage.game.genre.split(', ') if homepage.game.genre else []
    updates = homepage.updates.all().order_by('-update_date')
    game = homepage.game

    # game average rating
    average_rating = calculate_average_rating(game)
    game.game_rating = average_rating
    game.save()

    #progess value/bar color
    progress_value, bar_color = get_stage_info(homepage.game.stage)

    #disable the submit button
    has_rated = {}
    for update in updates:
        has_rated[update.id] = get_rating_status(request.user.userprofile, update.id)

    is_game_owner = game.owner == request.user.userprofile
        



    # rendering
    return render(
        request, 'game/gameHomepage.html', {
            'game': homepage.game,
            'homepage': homepage,
            'genres': genres,
            'progress_value': progress_value,
            'bar_color': bar_color,
            'updates': updates,
            'average_rating': average_rating,
            'total_updates': updates.count(),
            'has_rated': has_rated,
            'is_game_owner': is_game_owner,
 
        }
    )




