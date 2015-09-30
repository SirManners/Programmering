__author__ = 'ab53995'

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

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_mode((1366,768),pygame.FULLSCREEN)

"""
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kapitel 5")
"""

snow_list = []
for i in range(50):
    x = random.randrange(0, 1366)
    y = random.randrange(0, 768)
    snow_list.append([x, y])

done = False
clock = pygame.time.Clock()
rekt_x = 50
rekt_y = 50
rekt_change_x = 5
rekt_change_y = 5
y_mouse =
x_mouse =
while not done:
    for event in pygame.event.get():
        # Gör att programet stängs när man trycker på en knapp
        if event.type == pygame.KEYDOWN:
            done = True
        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True

        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    screen.fill(NIGHTBLUE)

    """pygame.draw.rect(screen, WHITE, [rekt_x, rekt_y, 50, 50])
    pygame.draw.rect(screen, RED, [rekt_x + 10, rekt_y + 10, 30, 30])
    rekt_x += rekt_change_x
    rekt_y += rekt_change_y
    if rekt_x > 1316 or rekt_x < 0:
        rekt_change_x *= -1
    if rekt_y >718 or rekt_y < 0:
        rekt_change_y *= -1"""

    """for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 768:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 1366)
            snow_list[i][0] = x

"""

    text_2 = "x=", x_mouse, "\ny=", y_mouse
    font = pygame.font.SysFont('Courier New', 300, True, False)
    text = font.render(text_2, True, BLACK)
    screen.blit(text, [x_mouse, y_mouse])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
