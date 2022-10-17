from blackjack.suit import Suit


class Card:
    def __init__(self, rank: int, suit: Suit):
        self.rank = rank
        self.suit = suit
