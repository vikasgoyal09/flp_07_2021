from .. import models
from .. import serializer
from django.contrib.auth.models import User




def fetch_enrolled_games(request):
    '''
    fetches enrolled games from database
    '''
    user = User.objects.get(username=request.user.username)
    user_id = user.id
    gameboardlist = []
    gameplayer = models.GamePlayer.objects.filter(user_id=user_id)
    serializers = serializer.GamePlayerSerializer(gameplayer, many=True)
    for i in serializers.data:
        gameboardlist.append(i['game_id'])
    gameboard = models.GameBoardModel.objects.filter(
        id__in=gameboardlist).order_by('-start_time')
    gameboard_serializer = serializer.GameBoardSerializer(gameboard, many=True)
    content = gameboard_serializer.data
    return content
