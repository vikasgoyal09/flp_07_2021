from ..serializer import GamePlayerSerializer
from datetime import datetime, time

from background_task import background
from django.conf import settings
from ..models import GameBoardModel, GamePlayer, StatusChoice
from ..scheduler.live_games import GameRunner
from django.utils import timezone


# @background(schedule=10)
def check_active_games():
    # TODO fix this query to get all the pending game model objects
    game_objects = GameBoardModel.objects.filter(
        status=StatusChoice.PENDING.value, start_time__lte=timezone.now()
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
        settings.LIVE_GAME[game_object.id] = GameRunner(game_object, players_in_game_serialized)
        game_object.update(status=StatusChoice.LIVE.value)

#end game when timer ends
# @background(schedule=10)
def endgame():
    game_objects = GameBoardModel.objects.filter(
        status=StatusChoice.ACTIVE.value,
        end_time__lte=timezone.now()
    )
    for game_object in game_objects:
        game_object.status = StatusChoice.COMPLETED.value

        # del settings.LIVE_GAME[game_object.id]