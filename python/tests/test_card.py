import unittest

from blackjack.suit import Suit
from blackjack.card import Card


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.cards = [Card(rank, Suit.Clubs) for rank in range(1, 14)]

        # I know this is wierd, but that's just how Black Splits when PEP8 is in play
        self.cards_str = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "J",
            "Q",
            "K",
            "A",
        ]

    def test_show(self):
        card_to_str = list(map(str, self.cards))
        self.assertEqual(card_to_str, self.cards_str)

    def test_invalid_low(self):
        card = Card(0, Suit.Clubs)
        with self.assertRaises(RuntimeError):
            str(card)

    def test_invalid_high(self):
        card = Card(100, Suit.Clubs)
        with self.assertRaises(RuntimeError):
            str(card)
