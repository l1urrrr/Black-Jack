import random
import time


def run():
    while True:
       decision1 = input("Do you want to play a game of Black Jack? Type "
                      "'Y'/'N' ").upper()
       if decision1 == 'Y':
           play()
       elif decision1 == 'N':
           break
       else:
           print("invalid input. Please type 'Y' or 'N'")
           continue
       decision2 = input("Do you want to play another game? [Y/N]").upper()
       if decision2 == 'Y':
           while decision2:
            play()
            decision2 = input("Do you want to play another game? [Y/N]").upper()


       elif decision2 == 'N':
         break
       else:
        print("invalid input. Please type 'Y' or 'N'")


  #continue


def selection():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

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
        decision2 = input("Type 'y' to hit, type 'n' to pass:").upper()
    except :
        ValueError ("Please type 'y' or 'n'")


    if decision2 == 'Y':
        player_hand.append(selection())

    player_tot = sum(player_hand)
    dealer_tot = sum(dealer_hand)
    player_prox = abs(21 - player_tot)
    dealer_prox = abs(21 - dealer_tot)
    if player_prox < dealer_prox and player_tot <= 21 and dealer_tot<= 21 :
        print(f'your cards: [{[card for card in player_hand]}]')
        print(f"Dealer's cards:[{[card for card in dealer_hand]}]")
        time.sleep(0.5)
        print("Dealer's gone bust !you win!!")
    elif dealer_prox  < player_prox and player_tot <= 21 and dealer_tot<= 21:
        print(f'your cards: [{[card for card in player_hand]}]')
        print(f"Dealer's cards:[{[card for card in dealer_hand]}]")
        time.sleep(0.5)
        print("You've gone bust! Dealer wins!!")
    else:
        highest = max(player_prox,dealer_prox)
        if highest == player_prox and player_tot <= 21 and dealer_tot<= 21:
            print(f'your cards: [{[card for card in player_hand]}]')
            print(f"Dealer's cards:[{[card for card in dealer_hand]}]")
            time.sleep(0.5)
            print("You Win!!")
        elif highest == dealer_prox and player_tot <= 21 and dealer_tot <=21:
            print(f'your cards: [{[card for card in player_hand]}]')
            print(f"Dealer's cards:[{[card for card in dealer_hand]}]")
            time.sleep(0.5)
            print("Dealer Wins")
        else:
            print("idk who wins, Damn!")





print(run())
    