from ..models.common import AccountTransaction, EmptyCell

DEFAULT_HOTEL_TYPE = 'SILVER'
HOTEL_TYPE_CONFIG = {
    'SILVER': {
        'purchase_price': 200,
        'rent': 50,
        'next': 'GOLD'
    },
    'GOLD': {
        'purchase_price': 300,
        'rent': 150,
        'next': 'PLATINUM'
    },
    'PLATINUM': {
        'purchase_price': 500,
        'rent': 300
    }
}


class HotelCell(EmptyCell):
    def __init__(self):
        self.owner = None
        self.type = DEFAULT_HOTEL_TYPE
        hotel_config = HOTEL_TYPE_CONFIG[DEFAULT_HOTEL_TYPE]
        self.rent = hotel_config.get('rent')
        self.hotel_value = hotel_config.get('purchase_price')
        # This field annotate a current type of hotel can be upgraded to
        self.next = hotel_config.get('next')

    def on_land(self, bank: AccountTransaction, user: AccountTransaction):
        """
        If any user land on this subtract money from users account and transfer into central bank
        :param bank: Central bank
        :param user: User who land on Hotel cell
        :return action: Action performed by the Cell so it can be configure
        """
        if self.owner:
            # If owner lands on the cell upgrade the hotel
            if self.owner == user:
                self.__upgrade__(bank, user)
            # Else pay rent to the owner
            else:
                self.__pay_rent__(bank, user)
        else:
            #  If Hotel is not having owner it is available to purchase
            self.__buy_hotel__(bank, user)

    def __buy_hotel__(self, bank: AccountTransaction, user: AccountTransaction):
        """
        If hotel don't have any owner and user is having the money to buy this hotel
        perform this action, subtract money from user's account and transfer it in Central bank
        """
        amount = self.hotel_value
        # Subtract hotel value from from the user's account
        user.subtract_money(amount)
        # Pay money to the bank for hotel's value
        bank.add_money(amount)
        # Make user as a owner of the hotel
        self.owner = user
        # Update owners assets value
        self.owner.add_in_assets(amount)

    def __pay_rent__(self, bank: AccountTransaction, user: AccountTransaction):
        """
        If a hotel is pre-owned by different user than the landed user pay rent to the owner by
        subtracting rent amount from landed user's account and transferring it into owners account
        """
        amount = self.rent
        # Subtract hotel rent from from the user's account
        user.subtract_money(amount)
        # Add rent into the owners account
        self.owner.add_money(amount)

    def __upgrade__(self, bank: AccountTransaction, user: AccountTransaction):
        """
        If owner lands on his hotel upgrade the hotel by paying upgrade amount to Central bank
        """
        if self.next:
            hotel_config = HOTEL_TYPE_CONFIG[self.next]
            upgrade_amount = hotel_config.get('purchase_price') - self.hotel_value
            # Subtract hotel value from from the user's account
            self.owner.subtract_money(upgrade_amount)
            # Pay money to the bank for hotel's value
            bank.add_money(upgrade_amount)
            # Upgrade hotel config
            self.__add_hotel_config__(hotel_config)
            # Update owners assets value with upgrade amount
            self.owner.add_in_assets(upgrade_amount)
        else:
            print('Upgrade not allowed')

    def __add_hotel_config__(self, hotel_config):
        # Upgrade hotel config
        self.type = self.next
        self.rent = hotel_config.get('rent')
        self.hotel_value = hotel_config.get('purchase_price')
        self.next = hotel_config.get('next')
