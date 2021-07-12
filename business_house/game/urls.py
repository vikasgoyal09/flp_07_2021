from django.urls import path

from . import views

urlpatterns = [
    #Enter url paths
    path('newgames/', views.new_games_view, name='newgames')
]