from django.shortcuts import render
from ..model.game import Game


def user_library(request):
    user_profile = request.user.userprofile
    games = user_profile.games.all()  

    return render(request, 'game/userLibrary.html', {'games': games, 'user_profile': user_profile})
