from django.shortcuts import redirect, render
from . import models
from django.db import IntegrityError
from . import serializer
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .apis.fetch_enrolled_games_api import fetch_enrolled_games
from .apis.fetch_new_games_api import fetch_new_games

import random
now = timezone.now()


# display new available games
@login_required(login_url='/user/login/')
def new_games_view(request):
    content = fetch_new_games(request)
    return render(request, 'game/new_games.html', {"newgameslist": content})


# display enrolled games
@login_required(login_url='/user/login/')
def enrolled_game(request):
    content = fetch_enrolled_games(request)

    return render(request, 'game/enrolled_games.html', {'enrolledgames': content})


# api to enroll into any available new game
@login_required(login_url='/user/login/')
def enrolling(request, game_id):
    try:
        gameboard = models.GameBoard.objects.get(id=game_id)
        if gameboard.no_of_players<gameboard.max_players:
            user = User.objects.get(username=request.user.username)
            gameboard.no_of_players+=1
            gameplayer = models.GamePlayer(user_id=user, game_id=gameboard)
            gameplayer.save()
            gameboard.save()
            return render(request, 'game/new_games.html', {"message": game_id})
        else:
            return render(request, 'game/new_games.html', {"message": "sorry max players reached"})
    except IntegrityError as ie:
        return render(request, 'game/new_games.html', {"message": "you are already enrolled in this game"})


@login_required(login_url='/user/login/')
def playing_view(request, game_id):
    user = User.objects.get(username=request.user.username)
    gameplayer = models.GamePlayer.objects.filter(game_id=game_id)
    gameplayer_serializer = serializer.GamePlayerSerializer(gameplayer, many=True)
    players = []

    for i in gameplayer_serializer.data:
        players.append(i['user_id'])
    
    if user.id in players:
        print('player can play this game he is registered')
    else:
        print('user cant play this game coz he aint register')
        return redirect('/user/home/')

    return render(request, 'game/in_game_view.html', {'gameid': game_id, 'active_players': gameplayer_serializer.data})


# class Runner:
#     def __init__(self,cells,player_count):
#         cells = cells
#         player_count = player_count
#         board = GameBoard(cells, player_count, 5000, )

#     def go(self, player, dice):
#         self.board.move_player(player, dice)

@login_required(login_url='/user/login/')
def roll_dice(request, game_id):
    user = User.objects.get(username=request.user.username)
    user_id = user.id
    dice = random.randInt(1,6)
    print("i am rolling dice",dice)
    return redirect(f'/game/playing/{game_id}')