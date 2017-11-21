"""Deck class takes no parameters, creates a list of 52 unique Card objects."""

from random import shuffle

from card import *

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

if __name__ == "__main__":
    main()
