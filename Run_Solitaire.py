# GUI for running Solitaire in with PyGame

import pygame, sys
from pygame.locals import *
from deck import *
from Solitaire import *

TABLE_COLOR = pygame.Color(164, 22, 22)
EMPTY_SPACE_COLOR = pygame.Color(160,0,0)
TABLE_WIDTH = 1000
TABLE_HEIGHT = 800
CARD_WIDTH = 100
CARD_HEIGHT = 200
MARGIN = 20

pygame.init()
DISPLAYSURF = pygame.display.set_mode((TABLE_WIDTH,TABLE_HEIGHT))

pygame.display.set_caption('Solitaire!')
mousex = 0
mousey = 0

newDeck = Deck()
newDeck.fiftyTwo()

i = 1
for c in newDeck.cards:
    temp = pygame.image.load(str(i)+'.png')
    c.image = pygame.transform.scale(temp,(CARD_WIDTH, CARD_HEIGHT))
    i += 1

backImg = pygame.image.load('back.png')
backImg = pygame.transform.scale(backImg,(CARD_WIDTH, CARD_HEIGHT))

game = newGame(newDeck)

def drawTable(surface):
    # Draw Pile 
    surface.blit(backImg,(int(TABLE_WIDTH/8 - CARD_WIDTH/2) ,MARGIN))

    if game.playPile.getTopCard() == None:
        pygame.draw.rect(surface,EMPTY_SPACE_COLOR,(int(TABLE_WIDTH/4 - CARD_WIDTH/2),MARGIN, CARD_WIDTH, CARD_HEIGHT))
    else:
        surface.blit(game.playPile.getTopCard().image,(int(TABLE_WIDTH/4 - CARD_WIDTH/2), MARGIN))

    #Draw Foundation
    for i in range(4):
        if game.foundation.getDeck(i).getTopCard() == None:
            pygame.draw.rect(surface,EMPTY_SPACE_COLOR,(int((i+4)*TABLE_WIDTH/8 - CARD_WIDTH/2),MARGIN, CARD_WIDTH, CARD_HEIGHT))   
        else:
            surface.blit(game.foundation.getDeck(i).getTopCard().image,(int((i+4)*TABLE_WIDTH/8 - CARD_WIDTH/2), MARGIN))

while True:
    DISPLAYSURF.fill(TABLE_COLOR)
    drawTable(DISPLAYSURF)
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
