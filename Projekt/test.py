
import Projekt.Klasser
import pygame

# --- Globala konstanter ---
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

# --- Klasser ---


class Block(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colourkey(WHITE)

        pygame.draw.ellipse(self.image, colour, [0, 0, width, height])
        self.rect = self.image.get_rect()


def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                done = True
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done = True

        screen.fill(NIGHTBLUE)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

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