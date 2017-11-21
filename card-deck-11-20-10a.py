"""
Using classes, create a deck of playing cards.
The class should take a rank and suit as parameters
and should also set a property denoted whether or not the card
is flipped to show it's face or not.
"""

from deck import *

from player import *


class Strategy:
    """Strategy(file) reads strategy file that contains 3 comma separated values:
    player hand total, dealer up card/total, player action. These values are used to create
    Strategy object used during gameplay."""
    def __init__(self, file):
        # create read ready file object
        infile = open(file, 'r')
        # container list
        self.strategy =[]
        # for each line, strip \n, split into variables,
        # cast player,dealer as int
        # append container list w/ list: player, dealer, action
        for line in infile:
            player, dealer, action = line.split(',')
            player = int(player)
            dealer = int(dealer)
            self.strategy.append([player,dealer,action.strip()])

    def getAction(self, player_total, dealer_up):
        """getAction(player total, dealer up) iterates through strategy list
        looking for item that matches player total and dealer up total
        against. When found, returns the action item in that list """
        for item in self.strategy:
            # each item is list w/ possible player total, dealer up, and player action
            # iterate through the list to find list item that matches supplied
            # player total and dealer up
            print(item, 'item')
            if player_total == item[0] and dealer_up == item[1]:
                print("found")
                action = item[2]
                return action



def main():
    # create player object
    # create dealer object
    # create Strategy object for player
    # create deck object for game
    #try:
     #   num = abs(int(input("Enter integer number of hands for simulation: ")))
    #except:
    #    print("Enter only integer--no decimal point ")
    #    main()
    player = Player("Brent")
    dealer = Dealer("Dealer")
    playerStrategy = Strategy("basic.txt")
    myDeck = Deck()

    """Simulation loops for X times start here"""

    # player bets
    player.bet(10)

    # set up player and dealer with cards
    # add 2 cards to player_hand
    for i in range(2):
        card = myDeck.dealCard(player.getLocation())
        player.setHand(card)

    for card in player.hand:
        print(card.getValue(), "player card")

    print(player.getTotal(), 'player TOTAL')

    for i in range(2):
        card = myDeck.dealCard(dealer.getLocation())
        dealer.setHand(card)
        dealer.setUpcard(card)

    for card in dealer.hand:
        print(card.getValue(), "dealer card")

    print(dealer.getTotal(), 'dealer hand total')
    print(dealer.getUpcard(), "dealer's UPCARD")
    print(player.getTotal(), "Players total before if condition testing")

    if player.getTotal() > 16:
        action = 'stand'

    elif player.getTotal() < 9:
        action = 'hit'

    elif player.getTotal() == 21:
        player.setAction("BJ")

    else:
        print("strategy list accessed")
        action = playerStrategy.getAction(player.getTotal(),dealer.getUpcard())
    print("Player should", action)

    """
    To this point we have setup player and dealer hands
    and obtained the values we have to match in the strategy database: 
    player total, dealer upcard. 
    While loop for player play
    """


    print("{0:<10} {1:>7}".format(card.getRank(), card.getSuit()))

    while player.getAction() != "bust" or player.getAction() != "stand" or player.getAction() != 'BJ':
        if player.getTotal > 16:
            player.setAction("stand")

        elif player.getTotal < 9:
            player.setAction("hit")

        else:
            player.setAction(playerStrategy.getAction( player.getTotal(), dealer.getUpcard() ) )

    """Now we deal with dealer play, assuming player did not bust"""
    while dealer.getAction() != "bust" or dealer.getAction() != "stand":
        if dealer.getTotal() < 17:
            dealer.setAction("hit")
        elif dealer.getTotal() >= 17 and dealer.getTotal() <= 21:
            dealer.setAction("stand")
        elif dealer.getAction() == 'hit':
            # if hit, need to add card to dealers hand
            # this is a convoluted way to get a card from deck

            card = myDeck.dealCard(dealer.getLocation())
            dealer.setHand(card)

        elif dealer.getTotal() > 21:
            dealer.setAction("bust")



    """
    use basicStrategy
    find 
    strategyTotal = basicStrategy.strategy[0]
    strategyDealer = basicStrategy.strategy[1]
    find card in basicStrategy,
    action = basicStrategy.strategy[2]
    
    """

    while dealer != "bust" or dealer != "stands" or player != bust or player.getAction() != "win" or player.getAction() != "push":

        if player.getTotal() > dealer.getTotal():


        if player.getAction() == "BJ":
            player.addFunds(player.getBetAmount()*3/2 + player.getBetAmount())

        # player wins, bet x 2 to return original bet plus winings
        if player.getAction() == "win"
            player.addFunds(player.getBetAmount() * 2)


if __name__ == "__main__":
    main()
