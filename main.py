""""
Black Jack by Al Sweigart al@inventwithpython.com
classic card game also known as 21
*this verison does not have splitting or insurance*
"""
import random
import sys
import functions


# setting up the constants
# constants are variables just all upper case these values do not change

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

# list of chr codes cna be found at inventwithpython.com/charactermap

BACKSIDE = 'backside'


def main():
    print("""
    1) Try to get as close to 21 without going over.
    2) Kings, Queens, and Jack are worth 10 points.
    3) Aces are worth 1 or 11 points.
    4) (H) hit to take another card
    5) (S) stand to stop taking cards.
    6) On the first play, ypu can double(D) down to increase your bet
    but you must hit exactly one or more time before standing. 
    7) In case of a tie, the best os returned to the player.
    The dealer stops hitting at 17.   
    """)

    # player money
    money = 5000

    # main loop of the game
    while True:
        # checking if the player has ran out of money.
        if money <= 0:
            print("You're Broke")
            print("Good thing yu wherent playing with real money.")
            print("Thanks for playing")
            sys.exit()

        #Let the player enter their bet for this round
        print('Money: ', money)
        bet = functions.getBet(money)
        print(bet)

        # give the dealer and player two cards from the deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handles players action
        print('Bet: ', bet)

if __name__ == "__main__":
    main()
