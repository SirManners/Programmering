
# Name:        Camel
# Purpose:
#
# Author:      ab53995, Jonas Cederberg
#
# Created:     04-09-2015
# Copyright:   (c) ab53995 2015
# Licence:     <your licence>

from math import *
import random
import pygame


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN    = ( 77,   18,  18)
YELLOW   = ( 255, 251,   0)
BLUE     = (   0,   4, 255)
NIGHTBLUE =(  0,   1,   64)
STARBLUE = (159, 161, 252)
GREY = (50, 50, 82)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kapitel 5")

# alt. fullscreen, bilden är dock ritad i fönsterstorleken ovan
# size = (700, 500)
# screen = pygame.display.set_mode(size)
# pygame.display.set_mode((1366,768),pygame.FULLSCREEN)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True

    screen.fill(NIGHTBLUE)

    pygame.draw.polygon(screen, STARBLUE, [[0+300, 15+50], [10+300, 0+50], [20+300, 15+50]], 0)
    pygame.draw.polygon(screen, STARBLUE, [[0+300, 5+50], [10+300, 20+50], [20+300, 5+50]], 0)
    pygame.draw.polygon(screen, STARBLUE, [[0, 15], [10, 0], [20, 15]], 0)
    pygame.draw.polygon(screen, STARBLUE, [[0, 5], [10, 20], [20, 5]], 0)

    pygame.draw.rect(screen, GREY, [0, 300, 700, 200], 0)

    for x_offset in range(0, 700, 200):
        pygame.draw.rect(screen, BLACK, [0 + x_offset, 200, 100, 300], 0)

    pygame.draw.ellipse(screen, WHITE, [450, 75, 100, 100], 0)

    for y_offset in range(0, 700, 150):
        pygame.draw.rect(screen, YELLOW, [220, 250 + (y_offset / 2 ), 15, 20], 0)

    pygame.draw.rect(screen, BLACK, [0, 400, 700, 700], 0)

    for y_offset in range(0,700, 150):
        pygame.draw.rect(screen, YELLOW, [20, 300 + y_offset, 15, 20], 0)

    for y_offset in range(0,700, 150):
        pygame.draw.rect(screen, YELLOW, [470, 230 + y_offset, 15, 20], 0)

    for y_offset in range(0,700, 80):
        pygame.draw.rect(screen, YELLOW, [630, 230 + y_offset, 15, 20], 0)

    for x_offset in range(150, 700, 200):
        pygame.draw.rect(screen, GREY, [0 + x_offset, 100 + (x_offset / 10), 30, 200], 0)

    pygame.draw.rect(screen, BLACK, [410, 100, 25, 400], 0)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
