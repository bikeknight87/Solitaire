# This is a deck of cards

import random, sys

# A Card consists of a rank, suit and face(face up is True, face down is False).
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face = False
        self.image = None

    # Turn a card to a given face.
    def turn(self, face):
        self.face = face
        
    def printCard(self):
        print(self.rank,'\t\t',self.suit,'\t\t', self.face)

# A Deck is a list of cards.
class Deck:
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
        print('Rank','\t\t','Suit','\t\t','Face Up\n')
        for c in self.cards:
            c.printCard()
        print('\n')

    # Move a card from the top of this desk to destination deck
    def move(self,dest):
        dest.pushCard(self.pullCard())

    # Move a stack of cards of given size from the top of this deck to the destination deck.
    def moveStack(self, size, dest):
        temp = self.cut(size)
        temp.cards.reverse()
        for c in range(size):
            temp.move(dest)

    # Return the Card on top of this deck without removing it from the deck.
    def getTopCard(self):
        if not self.cards:
            #print('Empty')
            return None
        else:
            #self.cards[-1].printCard()
            return self.cards[-1]

    def getBottomCard(self):
        if not self.cards:
            return None
        else:
            self.cards[0].printCard()
            return self.cards[0]
        

    # Turn over the top card of this deck
    def turnTopCard(self):
        self.cards[-1].face = True
        

    # Create a traditional Fifty Two card deck
    def fiftyTwo(self):
        suits = ('Leaves','Acorns','Hearts','Bells')
        ranks = ('King','Queen','Jack','10','9','8','7','6','5','4','3','2','Ace')
        for s in suits:
            for r in ranks:
                self.pushCard(Card(r,s))
