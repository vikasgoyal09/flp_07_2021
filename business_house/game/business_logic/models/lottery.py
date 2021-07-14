from ..models.common import EmptyCell, AccountTransaction

LOTTERY_WINNINGS = 200


class LotteryCell(EmptyCell):

    def on_land(self, bank: AccountTransaction, user: AccountTransaction):
        """
        If any user land on this subtract money from bank and transfer into users account
        :param bank: Central bank
        :param user: User who received the lottery
        """
        # Subtract money from the central bank
        bank.subtract_money(LOTTERY_WINNINGS)
        # Pay money to the user
        user.add_money(LOTTERY_WINNINGS)
