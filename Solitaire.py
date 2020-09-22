# This is the game of Solitaire

from deck import *

DrawPile = Deck()
DrawPile.fiftyTwo()

class Foundations:
    def __init__(self):
        self.decks = list()
        for d in range(4):
            self.decks.append(Deck())

    # Return the deck object where 'which' is an integer between 1 and 4.
    def getDeck(self, which):
        return self.decks[which - 1]

    # Check to see wether the given foundation deck is full
    def isFull(self, which):
        temp = which.getTopCard()
        if temp.rank is 'King':
            return True
        else:
            return False

    # Check to see if a given move is a valid foundation move, The card being
    # placed must be of the same suit and of one value higher than the top card of
    # the deck it's being placed on. Which is an integer between 1 and 4, card 
    # is a card object.
    def isValid(self, which, card):
        top = self.decks[which-1].getTopCard()
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
        for d in range(7):
            self.decks.append(Deck())

    # return the deck object were 'which' is an integer between 1 and 7.
    def getDeck(self, which):
        return self.decks[which - 1] 

    # Deal Cards into the Tableau
    def fillTableau(self):
        DrawPile.shuffle()
        i = 0
        while i < 7:
            for d in range(i,7):
                DrawPile.move(self.decks[d])
            i += 1
        for d in self.decks:
            d.turnTopCard()

    # Print the decks in the tableau
    def printTableau(self):
        print('Tableau\n')
        for d in self.decks:
            d.printDeck()

    def isValid(self, which, deck):
        top = self.decks[which-1].getTopCard()
        if top is None:
            if deck.cards[0].rank is 'King':
                return True
            else:
                return False
        elif top.suit is 'Clubs' or top.suit is 'Spades':
            if deck.cards[0].suit is 'Hearts' or deck.cards[0] is 'Diamonds':
                return True
            else:
                return False
        else:
            if deck.cards[0].suit is 'Clubs' or deck.cards[0].suit is 'Spades':
                return True
            else:
                return False
