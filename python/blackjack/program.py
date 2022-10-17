from enum import Enum
from typing import List, Optional

from blackjack.card import Card
from blackjack.deck import Deck


class RoundStatus(Enum):
    lost = -1
    tie = 0
    won = 1


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
    hand_dealer: List[Card] = []

    # -1: Lost
    #  0: Tie
    #  1: Won
    status: Optional[RoundStatus] = None

    # Technically we could pull this card after the player is done, buts its more correct to do it now
    dealer_hidden_card = deck.cards.pop()

    # Players also start with a card in blackjack
    hand.append(deck.cards.pop())
    total = sum_hand(hand)

    hand_dealer.append(deck.cards.pop())
    total_dealer = sum_hand(hand_dealer)

    while True:

        print(f"Player has {total}, dealer has {total_dealer}")

        read = input("Stand, Hit:\n")
        if read == "Hit":
            card = deck.cards.pop()
            hand.append(card)
            total = sum_hand(hand)
            total_dealer = sum_hand(hand_dealer)

            print(f"Hit with {card.suit.name} {str(card)}. Total is {total}")
            print(f"Dealer has: {total_dealer}")

            # We the player busts the game is automatically over, without dealer intervention
            if total > 21:
                status = RoundStatus.lost
                break

        elif read == "Stand":
            hand_dealer.append(dealer_hidden_card)
            total_dealer = sum_hand(hand_dealer)

            print(
                f"Dealer flipped his hidden card {dealer_hidden_card.suit.name} {str(dealer_hidden_card)}, total of {total_dealer}"
            )
            while total_dealer < 17 and not total_dealer > total:
                card = deck.cards.pop()
                print(f"Dealer drew: {card.rank}")
                hand_dealer.append(card)
                total_dealer = sum_hand(hand_dealer)
                print(f"Dealer has: {sum_hand(hand_dealer)}")

            print(f"Dealer stopped at {total_dealer}, player har {total}")
            # At this point we know the player has not busted
            if total_dealer > 21:
                status = RoundStatus.won
            elif total == total_dealer:
                status = RoundStatus.tie
            elif total > total_dealer:
                status = RoundStatus.won
            elif total < total_dealer:
                status = RoundStatus.lost

            break

    if status == status.lost:
        print("Sorry, you lost!")
    elif status == status.tie:
        print("Its a tie!")
    elif status == status.won:
        print("You won!")
    else:
        raise RuntimeError()

    exit(status.value)


if __name__ == "__main__":
    main()
