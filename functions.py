import random
import sys
import main


def getbet(maxBet):
    """
    ask player how much they want to bet for this round
    """
    # keeps asking until theu enter a valid amount
    while True:
        print('Money much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet =input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # if the player enter a number, ask again
        if not bet.isdecimal():
            continue

        # player enters a valid bet
        bet =int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    """Return a list of (ranks, suits) tuples for all 52 cards."""
    deck = []
    for suits in (main.HEARTS, main.DIAMONDS, main.CLUBS, main.SPADES):
        for rank in range(2,11):
            # add the number to cards
            deck.append((str(rank), suits))
        for rank in ('J', 'Q', 'K', 'A'):
            # add the face and ace cards
            deck.append((rank, suits))
        random.shuffle(deck)
        return deck