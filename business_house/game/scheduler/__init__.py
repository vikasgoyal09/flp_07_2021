from datetime import datetime

from background_task import background
from django.conf import settings
from business_house.game.models import GameBoardModel, StatusChoice
from .live_games import GameRunner


@background(schedule=10)
def check_active_games():
    # TODO fix this query to get all the pending game model objects
    game_objects = GameBoardModel.objects.filter(
        status=StatusChoice.PENDING.value, start_time__lte=datetime.now()
    )
    # Iterate over all the pending game boards and create live runner for them
    for game_object in game_objects:
        settings.LIVE_GAME[game_object.id] = GameRunner(game_object)
        game_object.update(status=StatusChoice.LIVE.value)
