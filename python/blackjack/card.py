from blackjack.suit import Suit


class Card:
    def __init__(self, rank: int, suit: Suit):
        self.rank = rank
        self.suit: Suit = suit

    def __str__(self):
        if 0 < self.rank < 10:
            return str(self.rank)
        elif self.rank == 10:
            return "J"
        elif self.rank == 11:
            return "Q"
        elif self.rank == 12:
            return "K"
        elif self.rank == 13:
            return "A"
        else:
            raise RuntimeError(f"Card has illegal rank: {self.rank}")
