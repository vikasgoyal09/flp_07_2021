from ..models.common import AccountTransaction


class Player(AccountTransaction):
    def __init__(self, player_number):
        self.player_number = player_number
        self.amount_in_hand = 1000
        self.assets_value = 0
        self.current_cell_position = -1

    def __str__(self):
        return (
            f'Player-{self.player_number} has total money {self.amount_in_hand} and assets '
            f'amount: {self.assets_value}'
        )

    def __eq__(self, other):
        return self.player_number == other.player_number

    def balance(self):
        return self.amount_in_hand

    def add_money(self, amount):
        self.amount_in_hand += amount

    def subtract_money(self, amount):
        self.amount_in_hand -= amount

    def add_in_assets(self, amount):
        self.assets_value += amount
