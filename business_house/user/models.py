from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Wallet(models.Model):
    user_id = models.OneToOneField(User, on_delete=CASCADE)
    credit = models.IntegerField(default=1000)
