from ..business_logic.models.users import Player
from ..business_logic.common import GameBoard
from ..models import GameBoardModel


class GameRunner:
    def __init__(self, game_board_model: GameBoardModel, players_in_game):
        self.cells = game_board_model.cell_conf
        self.player_count = game_board_model.no_of_players
        #list of player playing game
        self.player_list = []
        self.board = GameBoard(self.cells, 5000)
        self.current_player = 0

        for i in players_in_game:
            self.player_list.append(Player(i['user_id']))

    def is_allowed_player(self, player, ):
        # TODO handle validation
        if self.player_list[self.current_player].player_number == player.id:
            return True
        else:
            return False
        # return self.current_player.pk == player.pk

    def roll_dice(self, dice_output):
        myplayer = self.player_list[self.current_player]
        self.board.move_player(myplayer, dice_output)
        # Set next player in current player
        self.current_player = (self.current_player+1)%len(self.player_list)

    def get_score(self):
        return self.player_list
