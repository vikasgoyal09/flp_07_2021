from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here

class GameBoard(models.Model):
    max_players = models.IntegerField()
    no_of_players = models.IntegerField(default=0)
    bank_amount = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cell_conf = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class GamePlayer(models.Model):
    game_id = models.ForeignKey(GameBoard, on_delete=CASCADE)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    scored_credit = models.IntegerField(default=0)

    def __str__(self):
        return "game_id: {} - user_id: {}".format(self.game_id, self.user_id)