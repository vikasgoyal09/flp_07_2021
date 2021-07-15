from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

from .common.choices import ChoiceEnum


class StatusChoice(ChoiceEnum):
    LIVE = 'LIVE'
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'


# Create your models here
# TODO fix this model Class name added Model as suffix
class GameBoardModel(models.Model):
    max_players = models.IntegerField()
    no_of_players = models.IntegerField(default=0)
    bank_amount = models.IntegerField(default=5000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cell_conf = models.CharField(max_length=255)
    status = models.CharField(choices=StatusChoice.choices(), max_length=20)

    def __str__(self):
        return str(self.id)

    @property
    def player(self):
        return GamePlayer.objects.filter(game_id=self.pk)


class GamePlayer(models.Model):
    game_id = models.ForeignKey(GameBoardModel, on_delete=CASCADE)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    scored_credit = models.IntegerField(default=0)

    class Meta:
        unique_together = ('game_id', 'user_id',)

    def __str__(self):
        return "game_id: {} - user_id: {}".format(self.game_id, self.user_id)
