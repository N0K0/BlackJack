from typing import List

from blackjack.card import Card
from blackjack.deck import Deck


def sum_hand(hand: List[Card]) -> int:
    aces = 0
    summation = 0
    for card in hand:
        if str(card) == "A":
            aces += 1

        summation = summation + card.rank

    for _ in range(aces):
        # Swap an ace from 11 to 1 if sum is higher than 21, if we run out of aces we return sum
        if summation > 21:
            summation -= 10

    return summation


def main():
    deck = Deck()
    hand: List[Card] = []

    while True:
        read = input("Stand, Hit:\n")

        if read == "Hit":
            card = deck.cards.pop()
            hand.append(card)
            total = sum_hand(hand)

            print(f"Hit with {card.suit.name} {card.rank}. Total is {total}")
            if total > 21:
                print(f"Sorry, you lost!")
                break

        elif read == "Stand":
            break


if __name__ == "__main__":
    main()
