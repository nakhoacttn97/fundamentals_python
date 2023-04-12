'''
Created on Dec 28, 2016

@author: KTPHUONG
'''
import pygame
from pygame.locals import *


screen = pygame.display.set_mode((1600,1200),0,32)
background = pygame.image.load("flower-backgrounds-7.jpg").convert()
# flower-png-27.png
image = pygame.image.load("flower-png-27.png").convert_alpha()

while True:
    screen.blit(background, (0,0))

    screen.blit(background, (10,10))

    pygame.display.update()