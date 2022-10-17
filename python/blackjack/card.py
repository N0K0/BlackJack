from blackjack.suit import Suit


class Card:
    def __init__(self, rank: int, suit: Suit):
        if rank <= 0:
            raise ValueError("Invalid card value")

        if rank >= 14:
            raise ValueError("Invalid card value")

        self._rank = rank
        self.suit: Suit = suit

    @property
    def rank(self):
        if self._rank == 1:
            return 11

        return min(self._rank, 10)

    def __str__(self):
        if 2 <= self._rank <= 10:
            return str(self.rank)
        elif self._rank == 1:
            return "A"
        elif self._rank == 11:
            return "J"
        elif self._rank == 12:
            return "Q"
        elif self._rank == 13:
            return "K"

    def __eq__(self, other):
        return self._rank == other._rank and self.suit.value == other.suit.value

    def __gt__(self, other):
        if self.suit.value > other.suit.value:
            return True

        if self._rank > other._rank:
            return True

        return False
