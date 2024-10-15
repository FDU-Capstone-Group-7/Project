from django.shortcuts import render
from ..model.game import Game


def user_library(request):
    user_profile = request.user.userprofile
    games = user_profile.games.all()  
    # avatar_url = user_profile.avatar.url if user_profile.avatar else '/static/Indie_Game/images/index.png'

    return render(request, 'game/userLibrary.html', {'games': games, 'user_profile': user_profile})
