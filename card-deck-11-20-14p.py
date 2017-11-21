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
            if player_total == item[0] and dealer_up == item[1]:
                print("Match found", item[0], item[1])
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
    for i in range(1):

        # player bets
        player.bet(10)

        # set up player and dealer with cards
        # add 2 cards to player_hand
        for i in range(2):
            # this assigns card to player location and adds to player hand list
            card = myDeck.dealCard(player.getLocation())
            player.setHand(card)

        #for card in player.hand:
        #    print(card.getValue(), "player card")

        print(player.getTotal(), 'player TOTAL')

        for i in range(2):
            card = myDeck.dealCard(dealer.getLocation())
            dealer.setHand(card)
            dealer.setUpcard(card)

        #for card in dealer.hand:
        #    print(card.getValue(), "dealer card")

        print(dealer.getUpcard(), "dealer's UPCARD")

        # print(player.getTotal(), "Players total before if condition testing")

        if player.getTotal() > 16:
            player.setAction("stand")

        elif player.getTotal() < 9:
            player.setAction("hit")

        elif player.getTotal() == 21:
            player.setAction("BJ")

        else:
            print("strategy list accessed")
            action = playerStrategy.getAction(player.getTotal(), dealer.getUpcard())
            player.setAction(action)
        print("Player should", player.getAction())

        """
        To this point we have setup player and dealer hands
        and obtained the values we have to match in the strategy database: 
        player total, dealer upcard. 
        While loop for player play
        """

        if dealer.getTotal() >= 17 and dealer.getTotal() <= 21:
            dealer.setAction("stand")


        else:
            dealer.setAction("hit")

        # NEED TO FIGURE OUT ABOUT DOUBLES
        # This loop takes care of all situations where player needs another card, namely player action of "hit"
        # Exits loop for bust, stand or BJ
        # while player.getAction() != 'BJ' or player.getAction() != "bust" or player.getAction() != "stand":
        while player.getAction() == "hit":
            # add another card to player's hand
            print("entered while loop")
            card = myDeck.dealCard(player.getLocation())
            player.setHand(card)
            print("Player total:",player.getTotal())

            # if player total between 17 and 21 inclusive, stand
            if player.getTotal() >= 17 and player.getTotal() <= 21:
                player.setAction("stand")

            # if player total less than 9 set to "hit"
            elif player.getTotal() < 9:
                player.setAction("hit")

            # if player total greater than 21 set to "bust"
            elif player.getTotal() > 21:
                player.setAction("bust")

            # for everything else, look up action in player strategy grid
            else:
                player.setAction(playerStrategy.getAction( player.getTotal(), dealer.getUpcard() ) )
            print("player action at end of while loop:", player.getAction())



        #Now we deal with dealer play, assuming player did not bust
        # Exits this loop on dealer bust or stand--wont' enter if player busts
        #while dealer.getAction() == "stand" or dealer.getAction() != "bust" or player.getAction() == "bust":
        while dealer.getAction() == "hit" and player.getAction() != "bust":
            card = myDeck.dealCard(dealer.getLocation())
            dealer.setHand(card)

            if dealer.getTotal() >= 17 and dealer.getTotal() <= 21:
                dealer.setAction("stand")
                print("Dealer action is", dealer.getAction())

            elif dealer.getTotal() > 21:
                dealer.setAction("bust")
                print("Dealer action is", dealer.getAction())

            elif dealer.getTotal() == player.getTotal():
                dealer.setAction("push")


        # We should have the result now. All action by player and dealer are complete.
        # If elif else loops that test each action condition that remains, BJ, win, push, bust

        # while dealer.getAction() != "bust" or dealer.getAction() != "stands" or player.getAction() != bust or player.getAction() != "win" or player.getAction() != "push":

        if player.getAction() == "BJ":
            player.addFunds(player.getBetAmount()*3/2 + player.getBetAmount())
            player.addWins()
            player.addBlackjacks()
            dealer.addLosses()

        elif player.getAction() == "bust":
            player.addBusts()
            player.addLosses()
            dealer.addWins()

        elif dealer.getAction() == "bust":
            player.setAction("win")
            player.addWins()
            dealer.addLosses()
            dealer.addBusts()

        elif player.getTotal() == dealer.getTotal():
            # When player bets, the money is considered the dealers,
            # so we return the bet amount when push occurs
            player.addFunds(player.getBetAmount())
            player.setAction("push")
            dealer.setAction("push")
            player.addPushes()
            dealer.addPushes()

        elif player.getTotal() > dealer.getTotal():
            player.setAction("win")
            player.addFunds(player.getBetAmount() * 2)
            player.addWins()
            dealer.addLosses()


        elif player.getTotal() < dealer.getTotal():
            player.setAction("loss")
            player.addFunds(player.getBetAmount() * 2)
            player.addLosses()
            dealer.addWins()







        print("Player", player.getTotal())
        print("Dealer", dealer.getTotal())
        print("Player", player.getAction())
        # reset player and dealer actions
        player.setAction("")
        dealer.setAction("")


if __name__ == "__main__":
    main()
