import pygame
import random
import main
import math

def colour():

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

    return ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY, SCREEN_HEIGHT, SCREEN_WIDTH

ROSA, \
BLACK, \
WHITE, \
GREEN, \
RED, \
BROWN, \
YELLOW, \
BLUE, \
NIGHTBLUE, \
STARBLUE, \
GREY, \
SCREEN_HEIGHT, \
SCREEN_WIDTH = \
    colour()

snow_list = [] #change name to stars?
for i in range(50):
    snow_x = random.randrange(0, 1366)
    snow_y = random.randrange(-768, 0)
    snow_list.append([snow_x, snow_y])


def text(screen, size, colour, message, x_offset, y_offset):
    font = pygame.font.SysFont("system bold", size)
    text = font.render(message, True, colour)
    center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) + x_offset
    center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2) + y_offset
    screen.blit(text, [center_x, center_y])


def stars(screen):
    for i in range(len(snow_list)):
            pygame.draw.circle(screen, WHITE, snow_list[i], 2)
            snow_list[i][1] += 5
            # fixa så att stjärnorna åker snabbare när man åker uppåt, och långsammare när man åker nedåt
            if snow_list[i][1] > 768:
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                x = random.randrange(0, 1366)
                snow_list[i][0] = x


class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = -500
        self.change_x = 0
        self.change_y = 3
        self.width = 1000
        self.height = 1300
        self.colour = BLACK

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])


class Stars(): # Fungerar ej...
    def __init_(self):
        self.star_list = []

        # AttributeError: 'Stjärnor' object has no attribute 'snow_list'

        for i in range(50):
            snow_x = random.randrange(0, 1366)
            snow_y = random.randrange(-768, 0)
            self.star_list.append([snow_x, snow_y])

    def draw_star(self, screen):
        for i in range(len(self.star_list)):
            pygame.draw.circle(screen, self.färg, self.star_list[i], 2)
            self.star_list[i][1] += 5
            if self.star_list[i][1] > 768:
                y = random.randrange(-50, -10)
                self.star_list[i][1] = y
                x = random.randrange(0, 1366)
                self.star_list[i][0] = x


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

"""class Text(): # TRASIG, istället bara göra en Text funktion?
    def __init__(self):
        self.size = 150
        self.font = pygame.font.SysFont("system bold", self.font)
        self.title = ""
        self.bold = True
        self.colour = WHITE

        # self.x = (SCREEN_WIDTH // 2) - (self.text.get_width() // 2)
        # self.y = (SCREEN_HEIGHT // 2) - (self.text.get_height() // 2)
        self.x = 0
        self.y = 0

    def render(self):
        self.text = self.font.render(self.title, self.bold, self.colour)

    def skriv(self, screen):

        screen.blit(self.text, [self.x, self.y])

        #self.gameover_message = graphics.Text
        #self.gameover_message.title = "Game Over"
        #self.gameover_message.render()
        #self.gameover_message.x = (SCREEN_WIDTH // 2) - (self.gameover_message.text.get_width() // 2)
        #wwself.gameover_message.y = (SCREEN_HEIGHT // 2) - (self.gameover_message.text.get_height() // 2)
"""