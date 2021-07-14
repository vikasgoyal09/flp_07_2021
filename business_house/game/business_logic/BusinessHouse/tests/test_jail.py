import unittest

from src.models.bank import CentralBank
from src.models.jail import JailCell
from src.models.users import Player


class TestJail(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = CentralBank()
        self.user = Player(1)
        self.jail = JailCell()

    def test_on_cell_land(self):
        self.jail.on_land(self.bank, self.user)
        self.assertEqual(self.bank.balance(), 5150, 'Bank balance should increase by jail fine')
        self.assertEqual(self.user.balance(), 850, 'User balance should decrease by jail fine')


if __name__ == '__main__':
    unittest.main()
