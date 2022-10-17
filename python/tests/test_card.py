import unittest
from operator import attrgetter

from blackjack.suit import Suit
from blackjack.card import Card


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.cards = [Card(rank, Suit.Clubs) for rank in range(1, 14)]
        # I know this is wierd, but that's just how Black Splits when PEP8 is in play
        self.cards_str = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]

        # Building our expected value with little finesse, as its simple
        self.expected_int = list(map(lambda v: min(v, 10), range(1, 14)))
        self.expected_int[0] = 11

        self.card_x1 = Card(rank=1, suit=Suit.Hearts)
        self.card_x2 = Card(rank=1, suit=Suit.Hearts)
        self.card_y1 = Card(rank=1, suit=Suit.Diamonds)
        self.card_y2 = Card(rank=1, suit=Suit.Diamonds)

        self.card_1a = Card(rank=1, suit=Suit.Hearts)
        self.card_1b = Card(rank=2, suit=Suit.Hearts)
        self.card_2a = Card(rank=1, suit=Suit.Diamonds)
        self.card_2b = Card(rank=2, suit=Suit.Diamonds)

    def test_str(self):
        card_to_str = list(map(str, self.cards))
        self.assertEqual(self.cards_str, card_to_str)

    def test_value(self):
        card_to_int = list(map(attrgetter("rank"), self.cards))
        self.assertEqual(card_to_int, self.expected_int)

    def test_invalid_low(self):
        with self.assertRaises(ValueError):
            Card(rank=0, suit=Suit.Clubs)

    def test_invalid_high(self):
        with self.assertRaises(ValueError):
            Card(rank=100, suit=Suit.Clubs)

    def test_eq(self):
        assert self.card_x1 == self.card_x2
        assert self.card_y1 == self.card_y2

    def test_gt(self):
        assert self.card_1a < self.card_1b
        assert self.card_2a < self.card_2b
        assert self.card_1b < self.card_2b
        assert self.card_1a < self.card_2a
