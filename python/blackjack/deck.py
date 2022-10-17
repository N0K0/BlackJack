from collections import deque

from blackjack.suit import Suit
from blackjack.card import Card
from random import shuffle


class Deck:
    def __init__(self):

        _lst = []
        for suit in Suit:
            for i in range(1, 14):
                _lst.append(Card(rank=i, suit=suit))
        shuffle(_lst)

        self.cards = deque(_lst)
        del _lst
