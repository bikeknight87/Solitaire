# This is a deck of cards

import random, pygame, sys
from pygame.locals import *

# A Card consists of a rank, suit and face(face up is True, face down is False).
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face = False

# Turn a card to a given face.
    def turn(self, face):
        self.face = face
        
    def printCard(self)
    print(self.rank,'\t\t',self.suit)

# A Deck is a list of cards.
class Deck
    def __init__(self):
        self.cards = list()

    def deckSize(self):
        return len(self.cards)

# Place a card on the top of a Deck.
    def pushCard(self, card):
        self.cards.append(card)

# Pull a card from the top of a Deck and return it.
    def pullCard(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

# Create and retrun a new Deck of size 'depth' from the top of the current Deck.
def cut(self,depth):
    if depth == 0:
        return self
    else:
        newDeck = Deck()
        for c in range(depth):
            newDeck.pushCard(self.pullCard())
            newDeck.cards.reverse()
        return newDeck

def printDeck(self):
    print('Rank','\t\t','Suit\n')
    for c in self.cards:
        c.printCard()
        print('\n')

# move a card from the top of this pile to destination deck
def move(self,dest):
    dest.pushCard(self.pullCard())

# return the Card on to pof this deck without removing it from the deck
def getCard(self):
    if not self.cards:
        print('empty')
        return
    else:
        self.cards[-1].printCard()
        return self.cards[-1]

def fiftyTwo(self):
    suits = ('Cups','Bells','Leaves','Acorns')
    ranks = ('King','Queen','Jack','10','9','8','7','6','5','4','3','2','Ace')
    for s in suits:
        for r in ranks:
            self.pushCard(Card(r,s))

class Foundations:
    def __init__(self):
        self.decks = [Deck(),Deck(),Deck(),Deck()]

def getDeck(self, dex):
    return self.decks[dex]

def isValid(self, card):
    if not deck.cards and card == Card('Ace','Spades'):
        return True
    elif card.rank > deck.cards
