# This is the game of Solitaire

from deck import *

class Foundation:
    def __init__(self):
        self.decks = list()
        for d in range(4):
            self.decks.append(Deck())

    # Return the deck object where 'which' is an integer between 0 and 3.
    def getDeck(self, which):
        return self.decks[which]

    # Check to see wether the given foundation deck is full
    def isFull(self, which):
        temp = which.getTopCard()
        if temp.rank is 'King':
            return True
        else:
            return False

    # Check to see if a given move is a valid foundation move, The card being
    # placed must be of the same suit and of one value higher than the top card of
    # the deck it's being placed on. Which is an integer between 0 and 3, card 
    # is a card object.
    def isValid(self, which, card):
        top = self.decks[which].getTopCard()
        if top is None:
            if card.rank is 'Ace':
                return True
            else:
                return False
        elif top.suit is not card.suit:
            return False
        elif card.rank is top.rank + 1:
            return True
        else:
            return False

    # Print the decks in the Foundation
    def printFoundation(self):
        print('Foundation\n')
        for d in self.decks:
            d.printDeck()

class Tableau:
    def __init__(self):
        self.decks = list()
        self.playDeck = Deck()
        for d in range(7):
            self.decks.append(Deck())

    # Deal Cards into the Tableau
    def fillTableau(self,deck):
        deck.shuffle()
        i = 0
        while i < 7:
            for d in range(i,7):
                deck.move(self.decks[d])
            i += 1
        for d in self.decks:
            d.turnTopCard()

    # Print the decks in the tableau
    def printTableau(self):
        print('Tableau\n')
        for d in self.decks:
            d.printDeck()

    def isValid(self, which, card):
        top = self.decks[which].getTopCard()
        if top is None:
            if card.rank is 'King':
                return True
            else:
                return False
        elif top.suit is 'Leaves' or top.suit is 'Acorns':
            if card.suit is 'Hearts' or card is 'Bells':
                return True
            else:
                return False
        else:
            if card.suit is 'Clubs' or card.suit is 'Spades':
                return True
            else:
                return False

class newGame:
    def __init__(self,deck):
        self.drawPile = deck
        self.playPile = Deck()
        self.foundation = Foundation()
        self.tableau = Tableau()