class EmptyCell:
    def on_land(self, bank, user):
        """
        When a dice rolls this function will called for the cell where user landed with bank and
        user as parameter
        This ust be implemented by all derived classes
        :param bank: Central bank
        :param user: Landed user
        """
        pass


class AccountTransaction:
    def add_money(self, amount):
        """
        Increase money by provided amount
        """
        pass

    def subtract_money(self, amount):
        """
        Decrease money by provided amount
        """
        pass

    def add_in_assets(self, amount):
        """
        If there is any upgrade in assets require it will be done in here
        """

    def balance(self):
        """
        return current balance in the account
        """
        pass
