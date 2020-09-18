# This is the game of Solitaire

from deck import *

class Foundations:
    def __init__(self):
        self.decks = list()
        for d in range(4):
            self.decks.append(Deck())

    # Return the deck object where which is an integer (1,2,3,4)
    def getDeck(self, which):
        return self.decks[which + 1]

    # Check to see wether the given foundation deck is full
    def isFull(self, which):
        temp = which.getTopCard()
        if temp.rank is 'King':
            return True
        else:
            return False

    # Check to see if a given move is a valid foundation move, The card being
    # placed must be of the same suit and of one value higher than the top card of
    # the deck it's being placed on.
    def isValid(self, deck, card):
        top = self.deck.getTopCard()

        if top is NULL and card.rank is 'Ace':
            return True

        if top.suit is not card.suit:
            return False
        elif top.rank is not card.rank - 1:
            return False
        else:
            return True

class Tableau:
    def __init__(self):
        self.decks = list()
        for d in range(7):
            self.decks.append(Deck())
   
    def getDeck(self, which):
        return self.decks[which + 1] 

    def fillTableau(self, deck):
        deck.shuffle()
        i = 0
        while i < 7:
            for d in range(i,7):
                deck.move(self.decks[d])
            i += 1

        for d in self.decks:
            d.turnTopCard()

    def printTableau(self):
        for d in self.decks:
            d.printDeck()
