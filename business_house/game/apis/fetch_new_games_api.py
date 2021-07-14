from .. import models
from .. import serializer
from django.contrib.auth.models import User
from django.db.models import F
from django.utils import timezone
now = timezone.now()


def fetch_new_games(request):
    '''
    fetches new available games from database
    ''' 
    user = User.objects.get(username=request.user.username)
    user_id = user.id
    gameplayer = models.GamePlayer.objects.filter(user_id=user_id)
    serializers_game_player = serializer.GamePlayerSerializer(
        gameplayer, many=True)
    gameboardlist = []
    for i in serializers_game_player.data:
        gameboardlist.append(i['game_id'])
    gameboard = models.GameBoardModel.objects.filter(start_time__gt=now, no_of_players__lt=F(
        'max_players')).exclude(id__in=gameboardlist).order_by('start_time')
    serializers = serializer.GameBoardSerializer(gameboard, many=True)
    content = serializers.data
    return content
