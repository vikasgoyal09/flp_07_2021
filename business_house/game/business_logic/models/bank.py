from ..models.common import AccountTransaction


class CentralBank(AccountTransaction):
    def __init__(self, initial_amount=5000):
        self.amount_in_hand = initial_amount

    def __str__(self):
        return f'Balance at Bank: {self.amount_in_hand}'

    def balance(self):
        return self.amount_in_hand

    def add_money(self, amount):
        self.amount_in_hand += amount

    def subtract_money(self, amount):
        self.amount_in_hand -= amount
