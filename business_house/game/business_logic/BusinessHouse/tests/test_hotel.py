import unittest

from src.models.bank import CentralBank
from src.models.hotel import HotelCell
from src.models.users import Player


class TestHotel(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = CentralBank()
        self.user_1 = Player(1)
        self.user_2 = Player(2)
        self.hotel_1 = HotelCell()

    def test_on_cell_land(self):
        self.hotel_1.on_land(self.bank, self.user_1)
        self.assertEqual(self.bank.balance(), 5200, 'Bank balance should increase by hotel value')
        self.assertEqual(self.user_1.balance(), 800, 'User balance should decrease by hotel value')
        self.assertEqual(
            self.hotel_1.owner, self.user_1, 'User should be added as a owner of the hotel'
        )

    def test_on_cell_land_again(self):
        self.hotel_1.on_land(self.bank, self.user_1)
        self.assertEqual(self.bank.balance(), 5200, 'Bank balance should increase by hotel value')
        self.assertEqual(self.user_1.balance(), 800, 'User balance should decrease by hotel value')
        self.assertEqual(
            self.hotel_1.owner, self.user_1, 'User should be added as a owner of the hotel'
        )

        # As owner again landed on the hotel so it should upgrade the hotel
        self.hotel_1.on_land(self.bank, self.user_1)
        self.assertEqual(
            self.bank.balance(), 5300, 'Bank balance should increase by hotel upgrade value'
        )
        self.assertEqual(
            self.user_1.balance(), 700, 'User balance should decrease by hotel upgrade value'
        )
        self.assertEqual(
            self.hotel_1.type, 'GOLD', 'Hotel type should be gold as it upgraded'
        )
        self.assertEqual(
            self.user_1.assets_value, 300,
            'Hotel type is gold so user assets value should increase'
        )

    def test_on_cell_land_max_hotel_types(self):
        self.hotel_1.on_land(self.bank, self.user_1)
        self.hotel_1.on_land(self.bank, self.user_1)
        self.hotel_1.on_land(self.bank, self.user_1)
        self.hotel_1.on_land(self.bank, self.user_1)
        self.hotel_1.on_land(self.bank, self.user_1)
        self.assertEqual(
            self.bank.balance(), 5500, 'Bank balance should increase by hotel upgrade value'
        )
        self.assertEqual(
            self.user_1.balance(), 500, 'User balance should decrease by hotel upgrade value'
        )
        self.assertEqual(
            self.hotel_1.type, 'PLATINUM', 'Hotel type should be gold as it upgraded'
        )
        self.assertEqual(
            self.user_1.assets_value, 500,
            'Hotel type is platinum so user assets value should be 500'
        )

    def test_on_cell_land_other_user(self):
        self.hotel_1.on_land(self.bank, self.user_1)
        self.assertEqual(self.bank.balance(), 5200, 'Bank balance should increase by hotel value')
        self.assertEqual(self.user_1.balance(), 800, 'User balance should decrease by hotel value')

        # As owner again landed on the hotel so it should upgrade the hotel
        self.hotel_1.on_land(self.bank, self.user_2)
        self.assertEqual(
            self.user_1.balance(), 850, 'User 1 received a rent from the user 2'
        )
        self.assertEqual(
            self.user_2.balance(), 950, 'User 2 paid the rent to the user 1'
        )


if __name__ == '__main__':
    unittest.main()
