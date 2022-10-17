import unittest

from blackjack.program import sum_hand
from blackjack.suit import Suit
from blackjack.deck import Card


class ProgramTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hands = [
            [
                Card(rank=10, suit=Suit.Clubs),
                Card(rank=10, suit=Suit.Clubs),
            ],
            [
                Card(rank=2, suit=Suit.Clubs),
                Card(rank=2, suit=Suit.Clubs),
            ],
            [
                Card(rank=11, suit=Suit.Clubs),
                Card(rank=11, suit=Suit.Clubs),
            ],
            [
                Card(rank=10, suit=Suit.Clubs),
                Card(rank=12, suit=Suit.Clubs),
            ],
            [
                Card(rank=13, suit=Suit.Clubs),
                Card(rank=13, suit=Suit.Clubs),
            ],
            [
                Card(rank=13, suit=Suit.Clubs),
                Card(rank=13, suit=Suit.Clubs),
                Card(rank=13, suit=Suit.Clubs),
            ],
            [
                Card(rank=10, suit=Suit.Clubs),
                Card(rank=11, suit=Suit.Clubs),
                Card(rank=12, suit=Suit.Clubs),
            ],
            [
                Card(rank=10, suit=Suit.Clubs),
                Card(rank=11, suit=Suit.Clubs),
                Card(rank=12, suit=Suit.Clubs),
                Card(rank=13, suit=Suit.Clubs),
            ],
            [
                Card(rank=1, suit=Suit.Clubs),
                Card(rank=1, suit=Suit.Clubs),
            ],
            [
                Card(rank=1, suit=Suit.Clubs),
                Card(rank=1, suit=Suit.Clubs),
                Card(rank=1, suit=Suit.Clubs),
            ],
            [
                Card(rank=1, suit=Suit.Clubs),
                Card(rank=1, suit=Suit.Clubs),
                Card(rank=1, suit=Suit.Clubs),
                Card(rank=1, suit=Suit.Clubs),
            ],
        ]

    def test_summation(self):
        expected_sums = [20, 4, 20, 20, 20, 30, 30, 40, 12, 13, 14]
        sums = list(map(lambda hand: sum_hand(hand), self.hands))

        self.assertEqual(expected_sums, sums)
