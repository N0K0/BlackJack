from typing import List

from blackjack.card import Card
from blackjack.deck import Deck


def main():

    deck = Deck()
    hand: List[Card] = []

    while True:
        read = input('Stand, Hit:\n')

        if read == 'Hit':
            card = deck.cards.pop()
            hand.append(card)
            total = sum([min(card.rank, 10) for card in hand])
            print(f'Hit with {card.suit.name} {card.rank}. Total is {total}')
        elif read == 'Stand':
            break


if __name__ == '__main__':
    main()
