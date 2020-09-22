# GUI for running Solitaire in with PyGame

import pygame, sys, Solitaire
from pygame.locals import *

TABLE_COLOR = pygame.Color(164, 22, 22)


pygame.init()
DISPLAYSUF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Solitaire!')

while True:
    for event in pygame.event.get():
        
