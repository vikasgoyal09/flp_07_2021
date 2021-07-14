import unittest

from src.models.bank import CentralBank
from src.models.lottery import LotteryCell
from src.models.users import Player


class TestLottery(unittest.TestCase):
    def setUp(self) -> None:
        self.bank = CentralBank()
        self.user = Player(1)
        self.lottery = LotteryCell()

    def test_on_cell_land(self):
        self.lottery.on_land(self.bank, self.user)
        self.assertEqual(
            self.bank.balance(), 4800, 'Bank balance should decrease by lottery amount'
        )
        self.assertEqual(
            self.user.balance(), 1200, 'User balance should increase by lottery winnings'
        )


if __name__ == '__main__':
    unittest.main()
