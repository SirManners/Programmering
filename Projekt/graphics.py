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


class Stjärnor():
    def __init_(self):
        self.färg = WHITE
        self.snow_list = []
        # AttributeError: 'Stjärnor' object has no attribute 'snow_list'

        for i in range(50):
            snow_x = random.randrange(0, 1366)
            snow_y = random.randrange(-768, 0)
            self.snow_list.append([snow_x, snow_y])

    def draw_snow(self, screen):
        for i in range(len(self.snow_list)):
            pygame.draw.circle(screen, self.färg, self.snow_list[i], 2)
            self.snow_list[i][1] += 5
            if self.snow_list[i][1] > 768:
                y = random.randrange(-50, -10)
                self.snow_list[i][1] = y
                x = random.randrange(0, 1366)
                self.snow_list[i][0] = x


def text(screen, size, colour, message, x_offset, y_offset):
    font = pygame.font.SysFont("system bold", size)
    text = font.render(message, True, colour)
    center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) + x_offset
    center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2) + y_offset
    screen.blit(text, [center_x, center_y])


class Text(): # TRASIG, istället bara göra en Text funktion?
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