"""Example BlackJack by Ryan Buck"""

import random

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace'
]

# Value dictionary for each rank
VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11,
}

DEALER_CUTOFF = 17


def create_deck() -> list:
    """Generates a new deck."""
    deck = []

    # Populate deck with all 52 cards
    for suit in SUITS:
        for rank in RANKS:
            deck.append({
                "rank": rank,
                "suit": suit,
            })

    random.shuffle(deck)
    return deck


def calc_hand_value(hand: list) -> int:
    """Calculates the value of a blackjack hand."""
    hand_value = 0
    ace_count = 0

    # Sums the values of the cards
    # Counts aces as 11, but keeps track of them to handle more later
    for card in hand:
        card_rank = card["rank"]
        hand_value += VALUES[card_rank]

        # Keep track of aces so their values can be handled later
        if card_rank == "Ace":
            ace_count += 1

    # Counts aces as 1 if it would be better for the hand
    while hand_value > 21 and ace_count > 0:
        ace_count -= 1

        # Because we counted aces as 11 earlier, if we want to count them as 1
        # now, all we have to do is subtract 10 from the hand value
        hand_value -= 10

    return hand_value


def show_hands(player_hand, dealer_hand, show_dealer_card = False) -> None:
    print()  # For the newline

    if not show_dealer_card:
        print("Dealer's Hand (?):")
        print("  ???")
        for card in dealer_hand[1:]:
            print(f"  {card["rank"]} of {card["suit"]}")
    else:
        print(f"Dealer's Hand ({calc_hand_value(dealer_hand)}):")
        for card in dealer_hand:
            print(f"  {card["rank"]} of {card["suit"]}")

    print(f"Your Hand ({calc_hand_value(player_hand)}):")
    for card in player_hand:
        print(f"  {card["rank"]} of {card["suit"]}")


def main():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Check for instant wins
    if calc_hand_value(dealer_hand) == 21 and calc_hand_value(player_hand) == 21:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("Tie!\n")
        return
    elif calc_hand_value(dealer_hand) == 21:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("Dealer wins!\n")
        return
    elif calc_hand_value(player_hand) == 21:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("You win!\n")
        return

    # Player turn
    show_hands(player_hand, dealer_hand)
    while calc_hand_value(player_hand) < 21:
        choice = input("Hit or stand? (h/s): ").lower()

        if choice == 'h':
            player_hand.append(deck.pop())
            show_hands(player_hand, dealer_hand)
        elif choice == 's':
            break
        else:
            print("ERROR: Invalid input!")

    # Check player status
    if calc_hand_value(player_hand) == 21:
        print("You win!\n")
        return
    if calc_hand_value(player_hand) > 21:
        print("You busted! Dealer wins!\n")
        return

    # Dealer turn
    while calc_hand_value(dealer_hand) < DEALER_CUTOFF:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        dealer_hand.append(deck.pop())
        input("Press enter to continue...")

    # Determine winner
    if calc_hand_value(dealer_hand) > 21:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("Dealer busted! You win!\n")
    elif calc_hand_value(player_hand) > calc_hand_value(dealer_hand):
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("You win!\n")
    elif calc_hand_value(dealer_hand) > calc_hand_value(player_hand):
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("Dealer wins!\n")
    else:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        print("Tie!\n")


if __name__ == "__main__":
    main()
