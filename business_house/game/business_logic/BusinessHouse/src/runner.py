from .common import GameBoard
from .input_provider import InputProviderFactory


# Get input
input_provided = InputProviderFactory.get_input_provider()
game_input = input_provided.get_input()

cells = game_input.get('cells')
dice_output = game_input.get('dice_output')
player_count = game_input.get('player_count')

# Create board for the players and cell objects
board = GameBoard(cells, player_count, 5000, )

for index, dice_number in enumerate(dice_output):
    board.move_player(index, dice_number)

# Result
for player in board.players:
    print(str(player))

print(str(board.central_bank))
