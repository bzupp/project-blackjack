"""
Using classes, create a deck of playing cards.
The class should take a rank and suit as parameters
and should also set a property denoted whether or not the card
is flipped to show it's face or not.
"""

"""Deck class takes no parameters, creates a list of 52 unique Card objects."""

from random import shuffle

"""Playing card class. Assigns """

class Card:
    """Card constructed w/ rank, suit, value"""
    def __init__(self, rank, suit, value):
        # rank could be value, A messes that up
        # Again, if graphics used, rank is needed info
        self.rank = rank
        # suit is relevant in BJ but if graphics used, needed info
        self.suit = suit
        # values set to card...Need to have exception for Aces
        self.value = value
        # Set location of card: deck (default), dealer, player, discard
        self.location = "deck"

    # GETTERS
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getLocation(self):
        return self.location

    # SETTERS
    def setLocation(self, location):
        self.location = location



class Deck:

    """Create a deck object containing Card objects"""
    def __init__(self):
        # Lists w/ possible suit and rank values
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        # Container list for deck
        self.deck = []
        # Nested for loops iterate through lists to produce a "deck" list
        # iterate through suits list
        for suit in suits:
            # for each suit, enter another for loop that loops len(ranks) times
            for i in range(len(ranks)):
                # append the deck object with the Card object
                # using i as index selector in ranks and values list
                self.deck.append(Card(ranks[i], suit, values[i]))
                # shuffle deck. Can't think of reason to do this separately
        # Shuffle the deck w/ random's shuffle method
        for char in "I want to be thoroughly shuffled, so shuffle me lots of times, please!":
            shuffle(self.deck)

    def getDeck(self):
        return self.deck

    def dealCard(self, location):
        """NOT TESTED YET. RETURNS NEXT DECK LOCATION CARD IN DECK"""
        for card in self.deck:
            if card.getLocation() == "deck":
                card.setLocation(location)
                return card




"""Player class  initializes Hands dealt, wins, losses, pushes"""

class Player:
    """Player(funds) object takes the amount of money the player starts with (funds)
    aa a parameter and initializes other values: Hands dealt, wins, losses, pushes"""
    def __init__(self, name):
        self.wins = 0
        self.losses = 0
        self.pushes = 0
        self.busts = 0
        self.blackjacks = 0
        self.hands_dealt = 0
        self.funds = 0
        self.hand = []
        self.hand_total = 0
        self.location = name
        self.action = ""
        self.betAmount = 0

    def addBlackjacks(self):
        self.blackjacks = self.blackjacks + 1

    def getBlackjacks(self):
        return self.blackjacks

    def addWins(self):
        self.wins = self.wins + 1

    def getWins(self):
        return self.wins

    def addLosses(self):
        self.losses = self.losses + 1

    def getLosses(self):
        return self.losses

    def addPushes(self):
        self.pushes = self.pushes + 1

    def addBusts(self):
        self.busts = self.busts + 1

    def getBusts(self):
        return self.busts

    def getHandsDealt(self):
        self.hands_dealt = self.losses + self.wins + self.pushes + self.busts
        return self.hands_dealt

    def setAction(self, action):
        self.action = action

    def getAction(self):
        return self.action

    def addFunds(self, money_won):
        self.funds = self.funds + money_won

    def subFunds(self, money_lost):
        self.funds = self.funds - money_lost

    def getFunds(self):
        return self.funds

    def bet(self, bet):
        # bet per hand, removed from stake
        # not sur this is good approach
        self.betAmount = bet
        self.funds = self.funds - self.betAmount

    def getBetAmount(self):
        return self.betAmount

    def setHand(self, card):
        self.hand.append(card)

    def getHand(self):
        return self.hand

    def getTotal(self):
        # need to reset to 0 or total accumulates
        self.hand_total = 0
        for card in self.hand:
            self.hand_total = self.hand_total + card.getValue()
        return self.hand_total

    def getLocation(self):
        return self.location


class Dealer(Player):
    """Dealer is sub class of player, adds Upcard variable"""
    def __init__(self, name):
        super().__init__(name)
        self.upcard = 0

    def setUpcard(self, card):
        self.upcard = card.getValue()

    def getUpcard(self):
        return self.upcard



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
        # this assigns card to player location and adds to player hand list
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


    print("{0:<10} {1:>7}".format(card.getRank(), card.getSuit()))

    # NEED TO FIGURE OUT ABOUT DOUBLES
    # This loop takes care of all situations where player needs another card, namely player action of "hit"
    # Exits loop for bust, stand or BJ
    while player.getAction() != "bust" or player.getAction() != "stand" or player.getAction() != 'BJ':
        # add another card to player's hand
        card = myDeck.dealCard(player.getLocation())
        player.setHand(card)

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



    """Now we deal with dealer play, assuming player did not bust"""
    # Exits this loop on dealer bust or stand--wont' enter if player busts
    while dealer.getAction() != "bust" or dealer.getAction() != "stand" or player.getAction() != "bust":
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

    # We should have the result now. All action by player and dealer are complete.
    # If elif else loops that test each action condition that remains, BJ, win, push, bust


    # while dealer.getAction() != "bust" or dealer.getAction() != "stands" or player.getAction() != bust or player.getAction() != "win" or player.getAction() != "push":

    if player.getAction() == "BJ":
        player.addFunds(player.getBetAmount()*3/2 + player.getBetAmount())
        player.addWins()
        player.addBlackjacks()
        dealer.addLosses()

    elif player.getTotal() > dealer.getTotal():
        player.setAction("win")
        player.addFunds(player.getBetAmount() * 2)
        player.addWins()
        dealer.addLosses()

    elif player.getTotal() == dealer.getTotal():
        # When player bets, the money is considered the dealers,
        # so we return the bet amount when push occurs
        player.addFunds(player.getBetAmount())
        player.getAction("push")
        dealer.setAction("push")
        player.addPushes()
        dealer.addPushes()
    elif player.getAction() == "bust":
        player.addBusts()
        dealer.addWins()



    print("Player", player.getAction())
    # reset player and dealer actions
    player.setAction("")
    dealer.setAction("")


if __name__ == "__main__":
    main()
