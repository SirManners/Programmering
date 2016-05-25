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

star_list = []
for i in range(50):
    star_x = random.randrange(0, 1366)
    star_y = random.randrange(-768, 0)
    star_list.append([star_x, star_y])

def text(screen, size, colour, message, x_offset, y_offset):
    font = pygame.font.SysFont("system bold", size)
    text = font.render(message, True, colour)
    center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) + x_offset
    center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2) + y_offset
    screen.blit(text, [center_x, center_y])

def stars(screen):
    for i in range(len(star_list)):
            pygame.draw.circle(screen, WHITE, star_list[i], 2)
            star_list[i][1] += 5
            # fixa så att stjärnorna åker snabbare när man åker uppåt, och långsammare när man åker nedåt
            if star_list[i][1] > 768:
                y = random.randrange(-50, -10)
                star_list[i][1] = y
                x = random.randrange(0, 1366)
                star_list[i][0] = x

def rect(screen, x, y, width, height, colour):
    pygame.draw.rect(screen, colour, [x, y, width, height])

class Rectangle(): # denna klass gav mig felmeddelanden när jag ville använda funktionen draw
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
