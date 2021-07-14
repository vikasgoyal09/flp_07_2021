from ..models.common import EmptyCell, AccountTransaction

JAIL_FINE = 150


class JailCell(EmptyCell):

    def on_land(self, bank: AccountTransaction, user: AccountTransaction):
        """
        If any user land on this subtract money from users account and transfer into central bank
        :param bank: Central bank
        :param user: User who land on Jail
        """
        # Subtract money from user
        user.subtract_money(JAIL_FINE)
        # Pay money to central bank
        bank.add_money(JAIL_FINE)
