import random


def run():
    while True:
       decision1 = input("Do you want to play a game of Black Jack? Type "
                      "'Y'/'N' ")
       if decision1 == 'Y'.upper():
           continue
       elif decision1 == 'N'.upper():
           break
       else:
           print("invalid input. Please try again")
           continue
def selection():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.choice(cards)

def play():
    dealer_hand = []
    player_hand = []

    count = 0
    while count < 2:
        dealer_hand.append(selection())
        player_hand.append(selection())
        count += 1
    print(f'your cards: [{[card for card in player_hand]}]')
    print(f"dealer's  first card: {dealer_hand[0]}")

    try:
        decision2 = input("Type 'y' to hit, type 'n' to pass:")
    except :
        ValueError ("Please type 'y' or 'n'")


    if decision2 == 'y'.lower():
        player_hand.append(selection())
    player_tot = sum(player_hand)
    dealer_tot = sum(dealer_hand)
    player_prox = 21 - player_tot
    dealer_prox = 21 - dealer_tot
    if player_prox < dealer_prox and player_prox > 0:
     print("player wins!")

    print(f'your cards: [{[card for card in player_hand]}]')


    