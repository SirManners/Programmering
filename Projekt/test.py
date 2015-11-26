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

import pygame
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
# För att få fullscreen, siffrorna är skärmens upplösning
pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)


class Rektangel:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.change.x = 0
            self.change.y = 0
            self.bredd = 0
            self.höjd = 0
            self.färg = [255, 255, 255]

        def rörelse(self):
            self.x += self.change.x
            self.y += self.change.y

        def rita(self, screen):
            pygame.draw.rect(screen, self.färg, [self.x, self.y, self.bredd, self.längd])

ridå = Rektangel()
ridå.x = 0
ridå.y = -768
ridå.bredd = 1366
ridå.höjd = 768


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
    ridå.rörelse()
    ridå.rita(screen)
    # Printar allting på skärmen
    pygame.display.flip()
    # Hur många gånger per sekund som skärmen uppdateras
    clock.tick(60)

pygame.quit()


"""
rester

def meny_markör(markör_y):
        pygame.draw.rect(screen, WHITE, [150, markör_y, 30, 30])

    def meny_markör_rörelse(markör_y):
        if event.key == pygame.K_DOWN:
                if markör_y < 600:
                    markör_y += 100
                else:
                    pass
        elif event.key == pygame.K_UP:
                if markör_y > 300:
                    markör_y -= 100
                else:
                    pass
        return markör_y

markör_y = meny_markör_rörelse(markör_y)

meny_markör(markör_y)

"""