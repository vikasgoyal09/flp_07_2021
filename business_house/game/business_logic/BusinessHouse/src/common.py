from .models.bank import CentralBank
from .models.common import EmptyCell

from .models.hotel import HotelCell
from .models.jail import JailCell
from .models.lottery import LotteryCell
from .models.users import Player

# Data can change
CELLS_CONFIG = {
    'H': HotelCell,
    'L': LotteryCell,
    'J': JailCell,
    'E': EmptyCell
}


class CellFactory:
    @staticmethod
    def initialize(cell_type: str):
        try:
            return CELLS_CONFIG.get(cell_type)()
        except:
            raise Exception(f'Provide type({cell_type}) cell not available')


class GameBoard:
    def __init__(self, cells_input, players_count, bank_initial_amount):
        """
            Initialize the business board for the provide cells input and player count
        """
        self.central_bank = CentralBank(bank_initial_amount)
        self.cells = [CellFactory.initialize(cell_type) for cell_type in cells_input]
        self.players = [Player(i) for i in range(1, players_count + 1)]
        self.cell_count = len(self.cells)
        self.player_count = players_count

    def move_player(self, player_index, dice_value):
        # Move player for the received position
        current_player = self.players[player_index % self.player_count]
        # Get current player new cell position by adding steps in current position
        player_new_position = (current_player.current_cell_position + dice_value) % self.cell_count
        # Get cell where player land and perform on land function on the cell
        landing_cell = self.cells[player_new_position]
        landing_cell.on_land(self.central_bank, current_player)

        # Update player current cell position
        current_player.current_cell_position = player_new_position
