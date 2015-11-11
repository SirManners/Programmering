__author__ = 'ab53995'
import random
import pygame

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


class Rectangle:
    def __init__(self, x, y, xw, yw, xc, yc):
        self.x_value = x
        self.y_value = y
        self.x_width = xw
        self.y_width = yw
        self.change_x = xc
        self.change_y = yc

    def draw(self):
        pygame.draw.rect(screen, STARBLUE, [self.x_value, self.y_value, self.x_width, self.y_width])

    def move(self):
        self.x_value += self.change_x
        self.y_value += self.change_y

    def reset(self):
        if self.x_value > 1367 or self.x_value < 0:
            self.change_x *= -1
        if self.y_value > 769 or self.y_value < 0:
            self.change_y *= -1


class Ellipse(Rectangle):

    def draw(self):
        pygame.draw.ellipse(screen, STARBLUE, [self.x_value, self.y_value, self.x_width, self.y_width])

my_object = Rectangle
stuff =[]
for i in range(10):
    ellipse = Ellipse(random.randrange(0, 1367), random.randrange(0, 769), random.randrange(20, 70), random.randrange(20, 70), random.randrange(-3, 3), random.randrange(-3, 3))
    stuff.append(ellipse)
for i in range(10):
    rectangle = Rectangle(random.randrange(0, 1367), random.randrange(0, 769), random.randrange(20, 70), random.randrange(20, 70), random.randrange(-3, 3), random.randrange(-3, 3))
    stuff.append(rectangle)

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

    screen.fill(NIGHTBLUE)

    for rectangle in stuff:
        Rectangle.draw(rectangle)
        Rectangle.move(rectangle)
        Rectangle.reset(rectangle)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
