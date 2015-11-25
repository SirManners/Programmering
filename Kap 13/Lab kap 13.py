import pygame
import random

__author__ = 'ab53995'
# Färger, http://www.colorpicker.com/

ROSA    = ( 255, 0, 132)
BLACK     = (   0,   0,   0)
WHITE     = ( 255, 255, 255)
GREEN     = (   0, 255,   0)
RED       = ( 255,   0,   0)
BROWN     = (  77,  18,  18)
YELLOW    = ( 255, 251,   0)
BLUE      = (   0,   4, 255)
NIGHTBLUE = (   0,   1,  64)
STARBLUE  = ( 159, 161, 252)
GREY      = (  50,  50,  82)

player_image = pygame.image.load("player.png")


class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()


pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
# För att få fullscreen, siffrorna är skärmens upplösning
pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        # Gör att programet stängs när man trycker på en knapp
        if event.type == pygame.KEYDOWN:
            done = True
        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True

    # Färgen som fyller hela fönstret
    screen.fill(NIGHTBLUE)

    # Printar allting på skärmen
    pygame.display.flip()
    # Hur många gånger per sekund som skärmen uppdateras
    clock.tick(60)

pygame.quit()
