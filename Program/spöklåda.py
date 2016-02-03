__author__ = 'Mr.Orange'


__author__ = 'ab53995'

# Färger, http://www.colorpicker.com/

ROSA    = ( 255, 0, 132)
BLACK     = (   0,   0,   0)
WHITE     = ( 255, 255, 255)
MINDRE_VIT = (230, 231, 232)
ÄNNU_VIT = (196, 196, 196)
MINST_VIT = (145, 145, 145)
MINSTARE_VIT = (105, 105, 105)
GREEN     = (   0, 255,   0)
RED       = ( 255,   0,   0)
BROWN     = (  77,  18,  18)
YELLOW    = ( 255, 251,   0)
BLUE      = (   0,   4, 255)
NIGHTBLUE = (   0,   1,  64)
STARBLUE  = ( 159, 161, 252)
GREY      = (  50,  50,  82)
SCREEN_HEIGHT = 768
SCREEN_WIDTH = 1366
import pygame
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
# För att få fullscreen, siffrorna är skärmens upplösning
pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

y_m = 7
x_m = 7
x = 400
y = 300
x_coord = []
y_coord = []
i = -1

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

    x = x + x_m
    y = y + y_m

    x_coord.append(x)
    y_coord.append(y)
    i += 1

    if y_coord[i] >= SCREEN_HEIGHT - 50 or y_coord[i] <= 0:
        y_m *= -1
    if x_coord[i] >= SCREEN_WIDTH - 50 or x_coord[i] <= 0:
        x_m *= -1

    # Färgen som fyller hela fönstret
    screen.fill(BLACK)
    if i > 4:
        pygame.draw.rect(screen, MINSTARE_VIT, [x_coord[i-3], y_coord[i-3], 50, 50])
    if i > 3:
        pygame.draw.rect(screen, MINST_VIT, [x_coord[i-2], y_coord[i-2], 50, 50])
    if i > 2:
        pygame.draw.rect(screen, ÄNNU_VIT, [x_coord[i-1], y_coord[i-1], 50, 50])
    pygame.draw.rect(screen, WHITE, [x_coord[i], y_coord[i], 50, 50])


    # Printar allting på skärmen
    pygame.display.flip()

    # Hur många gånger per sekund som skärmen uppdateras
    clock.tick(60)

pygame.quit()
