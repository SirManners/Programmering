import pygame
import random
import main
import math

ROSA      = ( 255,   0, 132)
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
SCREEN_HEIGHT = 688
SCREEN_WIDTH = 1366
"""
class Grafik:
    def __init_(self):
        self.färg = WHITE
        self.

    def draw(self, screen):



class Stjärnor(Grafik):
    def __init__(self):
        super().__init__()

"""

# Asteroider

class Text(): # TRASIG
    def __init__(self):
        self.font = 36
        self.text = pygame.font.Font(None, self.font)
        self.title = ""
        self.bold = True
        self.colour = WHITE
        # self.x = (SCREEN_WIDTH // 2) - (self.text.get_width() // 2)
        # self.y = (SCREEN_HEIGHT // 2) - (self.text.get_height() // 2)
        self.x = 0
        self.y = 0


    def skriv(self, screen):
        self.text.render(self.title, self.bold, self.colour)
        screen.blit(self.title, [self.x, self.y])


class Rektangel():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.bredd = 0
        self.höjd = 0
        self.färg = [255, 255, 255]

    def rörelse(self):
        self.x += self.change_x
        self.y += self.change_y

    def rita(self, screen):
        pygame.draw.rect(screen, self.färg, [self.x, self.y, self.bredd, self.höjd])


class Ridå(Rektangel):
        def __init__(self):
            super().__init__()

        def rörelse(self):
            self.x += self.change_x
            if self.y >= -769:
                self.y += self.change_y