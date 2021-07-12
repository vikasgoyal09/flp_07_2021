from django.shortcuts import render
from . import models
from . import serializer
from django.utils import timezone
now = timezone.now()
# Create your views here.
def new_games_view(request):
    if request.user.is_authenticated:
        gameboard = models.GameBoard.objects.filter(start_time__gt = now ).order_by('start_time')
        serializers = serializer.GameBoardSerializer(gameboard, many=True)
        content = serializers.data
        print(content)
        ddd = {"name":"zain"}
    return render(request, 'game/new_games.html', {"newgameslist":content, "test":ddd})

def enroll_game(request):
    pass