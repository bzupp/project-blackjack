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


if __name__ == "__main__":
    main()
