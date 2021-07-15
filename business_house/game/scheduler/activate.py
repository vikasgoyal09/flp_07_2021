from django.http.response import HttpResponse
from ..serializer import GameBoardSerializer, GamePlayerSerializer
from datetime import datetime, time

from background_task import background
from django.conf import settings
from ..models import GameBoardModel, GamePlayer, StatusChoice
from ..scheduler.live_games import GameRunner
from django.utils import timezone


# @background(schedule=10)
def check_active_games(request):
    # TODO fix this query to get all the pending game model objects
    game_objects = GameBoardModel.objects.filter(
        status=StatusChoice.PENDING.value
    )
    # Iterate over all the pending game boards and create live runner for them
    print('scheduler ran')
    for game_object in game_objects:

        players_in_game = GamePlayer.objects.filter(
            game_id=game_object.id
        )
        players_in_game_serialized = GamePlayerSerializer(
            players_in_game,                                                        
            many=True
        )
        settings.LIVE_GAME[game_object.id] = GameRunner(game_object, players_in_game_serialized.data)
        print(settings.LIVE_GAME)
        # game_object.update(status=StatusChoice.LIVE.value)
        game_object.status = StatusChoice.LIVE.value
        game_object.save()
        print(game_object.status)

    return HttpResponse('activated successfully')

def endgame(request):
    game_objects = GameBoardModel.objects.filter(
        status=StatusChoice.LIVE.value
        # end_time__lte=timezone.now()
    )
    
    for game_object in game_objects:
        
        game_object.status = StatusChoice.COMPLETED.value
        game_object.save()
    return HttpResponse('game ended successfully')