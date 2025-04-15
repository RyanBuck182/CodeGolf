import random as r
p=print
l=list
#       0      1      2        3     4    5     6    7   8      9              10
allstr="Spades|Hearts|Diamonds|Clubs|Jack|Queen|King|Ace|Tie!\n|Dealer wins!\n|You win!\n".split('|')
SUITS=allstr[:4]
RANKS=l("23456789")+allstr[4:8]
VALUES=l(map(int,RANKS[:8]+[10]*3+[11]))
DEALER_CUTOFF = 17
def create_deck() -> list:
    deck=[]
    for suit in SUITS:
        for i,v in enumerate(RANKS):
            deck+=[(i,v,suit,VALUES[i])]
    r.shuffle(deck)
    return deck
def calc_hand_value(hand: list) -> int:
    hand_value=0
    ace_count=0
    for card in hand:hand_value+=card[3];ace_count+=1 if card[0]==11 else 0
    while hand_value>21 and ace_count>0:ace_count-=1;hand_value-=10
    return hand_value

def y(h):
    for c in h:p(f"  {c[1]} of {c[2]}")

def show_hands(player_hand, dealer_hand, show_dealer_card = False) -> None:
    print()
    if not show_dealer_card:
        print("Dealer's Hand (?):")
        print("  ???")
        y(dealer_hand[1:])
    else:
        print(f"Dealer's Hand ({calc_hand_value(dealer_hand)}):")
        y(dealer_hand)
    print(f"Your Hand ({calc_hand_value(player_hand)}):")
    y(player_hand)
def main():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
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
    if calc_hand_value(player_hand) == 21:
        print("You win!\n")
        return
    if calc_hand_value(player_hand) > 21:
        print("You busted! Dealer wins!\n")
        return
    while calc_hand_value(dealer_hand) < DEALER_CUTOFF:
        show_hands(player_hand, dealer_hand, show_dealer_card=True)
        dealer_hand.append(deck.pop())
        input("Press enter to continue...")
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