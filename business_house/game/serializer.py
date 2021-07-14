from rest_framework import serializers
from . import models


class GameBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameBoard
        fields = ['id', 'max_players', 'no_of_players', 'bank_amount', 'start_time', 'end_time', 'cell_conf']



class GamePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GamePlayer
        fields = ['game_id', 'user_id', 'scored_credit']