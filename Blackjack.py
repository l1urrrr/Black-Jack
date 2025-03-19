import random
import time
import art


def run():
    go = True
    while go:
       decision1 = input("Do you want to play a game of Black Jack? Type "
                      "'Y'/'N' ").upper()
       if decision1 == 'Y':
           print(art.logo)
           play()
       elif decision1 == 'N':
           break
       else:
           print("invalid input. Please type 'Y' or 'N'")
           continue
       decision2 = input("Do you want to play another game? [Y/N]").upper()
       if decision2 == 'Y':
           while decision2 == 'Y':
            play()
            decision2 = input("Do you want to play another game? [Y/N]").upper()
       elif decision2 == 'N':
         break
       else:
        while decision2 != 'Y' or 'N':
            print("invalid input. Please type 'Y' or 'N'")
            time.sleep(0.3)
            decision2 = input(
                "Do you want to play another game? [Y/N]").upper()




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
    decision2 = input("Type 'y' to hit, type 'n' to pass:").upper()

    if decision2 == 'Y':
        player_hand.append(selection())



    if dealer_hand[0]+dealer_hand[1] < 16:
        dealer_hand.append(selection())

    dealer_tot = sum(dealer_hand)
    player_tot = sum(player_hand)
    player_prox = abs(21 - player_tot)
    dealer_prox = abs(21 - dealer_tot)
    if player_tot <= 21 and dealer_tot <= 21 :
        if player_prox < dealer_prox:
            print(f'your cards: {[card for card in player_hand]}')
            print(f"Dealer's cards:{[card for card in dealer_hand]}")
            time.sleep(0.5)
            print("Dealer's gone bust !you win!!")
        elif dealer_prox < player_prox :
            print(f'your cards: {[card for card in player_hand]}')
            print(f"Dealer's cards:{[card for card in dealer_hand]}")
            time.sleep(0.5)
            print("You've gone bust! Dealer wins!!")
        elif player_prox == dealer_prox and player_tot :
            print(f'your cards: {[card for card in player_hand]}')
            print(f"Dealer's cards:{[card for card in dealer_hand]}")
            time.sleep(0.5)
            print("It's a draw!!")
        else:
            highest = max(player_prox,dealer_prox)
            if highest == player_prox and player_tot <= 21 and dealer_tot<= 21:
                print(f'your cards: {[card for card in player_hand]}')
                print(f"Dealer's cards:{[card for card in dealer_hand]}")
                time.sleep(0.5)
                print("You Win!!")
            elif highest == dealer_prox and player_tot <= 21 and dealer_tot <=21:
                print(f'your cards: {[card for card in player_hand]}')
                print(f"Dealer's cards:{[card for card in dealer_hand]}")
                time.sleep(0.5)
                print("Dealer Wins")
            else:
                print("idk who wins, Damn!")
                print(f'your cards: {[card for card in player_hand]}')
                print(f"Dealer's cards:{[card for card in dealer_hand]}")
    elif player_tot > 21 and dealer_tot <= 21 :
        print("you've gone bust! Dealer wins!")
        print(f'your cards: {[card for card in player_hand]}')
        print(f"Dealer's cards:{[card for card in dealer_hand]}")
    elif dealer_tot > 21 and player_tot <= 21:
        print(f'your cards: {[card for card in player_hand]}')
        print(f"Dealer's cards:{[card for card in dealer_hand]}")
        print("Dealer has gone bust! You win!")
    else:
        print("you've both gone bust! Nobody wins! ")


#TO DO:
#draw case: when the player and the dealer have the same amount in their
# hand then they draw
#if the dealer's total is less than 16 they have to pick up another card
#go over the logic of the game because sometimes the dealer is supposed to
# win either loses or draws



print(run())
    