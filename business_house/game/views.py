from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.db import IntegrityError
from . import serializer
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import F
now = timezone.now()


def new_games_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(username= request.user.username)
        user_id = user.id
        gameplayer = models.GamePlayer.objects.filter(user_id = user_id)
        serializers_game_player = serializer.GamePlayerSerializer(gameplayer, many=True)
        gameboardlist = []
        for i in serializers_game_player.data:
            gameboardlist.append(i['game_id'])
        gameboard = models.GameBoard.objects.filter(start_time__gt = now , no_of_players__lt=F('max_players')).exclude(id__in=gameboardlist).order_by('start_time')
        serializers = serializer.GameBoardSerializer(gameboard, many=True)
        content = serializers.data
    return render(request, 'game/new_games.html', {"newgameslist": content})

def enrolling(request, game_id):
    if request.user.is_authenticated:
        try:
            gameboard = models.GameBoard.objects.get(id=game_id)
            if gameboard.no_of_players<gameboard.max_players:
                user = User.objects.get(username=request.user.username)
                gameboard.no_of_players+=1
                gameplayer = models.GamePlayer(user_id=user, game_id=gameboard)
                gameplayer.save()
                gameboard.save()
                return render(request, 'game/new_games.html', {"message": game_id})
        except IntegrityError as ie:
            return render(request, 'game/new_games.html', {"message": "you are already enrolled in this game"})
    return render(request, 'game/new_games.html', {"message": "sorry max players reached"})

def enrolled_game(request):
    if request.user.is_authenticated:
        user= User.objects.get(username=request.user.username)
        user_id=user.id
        gameboardlist = []
        gameplayer=models.GamePlayer.objects.filter(user_id=user_id)
        serializers = serializer.GamePlayerSerializer(gameplayer, many=True)
        for i in serializers.data:
            gameboardlist.append(i['game_id'])
        gameboard = models.GameBoard.objects.filter(id__in=gameboardlist).order_by('-start_time')
        gameboard_serializer = serializer.GameBoardSerializer(gameboard, many=True)
        content = gameboard_serializer.data
        return render(request, 'game/enrolled_games.html', {'enrolledgames': content})
    return HttpResponse('Testing')