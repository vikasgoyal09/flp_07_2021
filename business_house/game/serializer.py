from rest_framework import serializers


class GameBoardSerializer(serializers.Serializer):
    max_players = serializers.IntegerField()
    no_of_players = serializers.IntegerField(default=0)
    bank_amount = serializers.IntegerField(default=5000)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    cell_conf = serializers.CharField(max_length=255)
