from django.utils.timezone import activate
from .scheduler.activate import check_active_games, endgame
from django.urls import path

from . import views

urlpatterns = [
    #Enter url paths
    path('newgames/', views.new_games_view, name='newgames'),
    path('newgames/<int:game_id>', views.enrolling, name= 'enrolling'),
    path('enrolledgames/', views.enrolled_game, name='enrolledgames'),
    path('playing/<int:game_id>', views.playing_view, name='playing'),
    path('rolldice/<int:game_id>', views.roll_dice, name='rolldice'),
    path('activate/', check_active_games, name='activate'),
    path('endgame', endgame, name='endgame'),
]