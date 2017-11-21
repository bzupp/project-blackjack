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

    def getPushes(self):
        return self.pushes

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

    def resetHand(self):
        self.hand = []

    def getTotal(self):
        # need to reset to 0 or total accumulates
        self.hand_total = 0
        for card in self.hand:
            self.hand_total = self.hand_total + card.getValue()
        # print("Hand total in player class", self.hand_total)
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



if __name__ == "__main__":
    main()
