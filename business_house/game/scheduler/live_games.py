from business_house.game.business_logic.common import GameBoard
from business_house.game.models import GameBoardModel


class GameRunner:
    def __init__(self, game_board_model: GameBoardModel):
        self.cells = game_board_model.cell_conf
        self.player_count = game_board_model.no_of_players
        self.board = GameBoard(self.cells, self.player_count, 5000)
        self.current_player = game_board_model.player.first()

    def is_allowed_payer(self, player, ):
        # TODO handle validation
        return self.current_player.pk == player.pk

    def roll_dice(self, player, dice_output):
        self.board.move_player(player, dice_output)
        # Set next player in current player
