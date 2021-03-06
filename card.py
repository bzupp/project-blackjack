"""Playing card class. Assigns """

class Card:
    """Card constructed w/ rank, suit, value"""
    def __init__(self, rank, suit, value, imagefile):
        # rank could be value, A messes that up
        # Again, if graphics used, rank is needed info
        self.rank = rank
        # suit is relevant in BJ but if graphics used, needed info
        self.suit = suit
        # values set to card...Need to have exception for Aces
        self.value = value
        # Set location of card: deck (default), dealer, player, discard.
        # Used to track where a card is.
        self.location = "deck"
        # name of image file for the card. The Deck class is creating this name
        # when a Deck instance is created, which creates the cards in the deck
        self.imagefile = imagefile

    # GETTERS
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def getLocation(self):
        return self.location

    def getImageFile(self):
        return self.imagefile

    # SETTERS
    def setLocation(self, location):
        self.location = location


if __name__ == "__main__":
    main()
