import unittest

from blackjack.deck import Deck


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_should_have_52_cards(self):
        self.assertEqual(52, len(self.deck.cards))

    def test_should_have_4_distinct_suits(self):
        self.assertEqual(4, len(set([card.suit for card in self.deck.cards])))

    def test_draw_order(self):
        pulled_deck = list(self.deck.cards)
        is_sorted = all(
            pulled_deck[i] < pulled_deck[i + 1] for i in range(len(pulled_deck) - 1)
        )
        assert not is_sorted
