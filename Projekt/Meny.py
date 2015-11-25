
__author__ = 'ab53995'
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


pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
# För att få fullscreen, siffrorna är skärmens upplösning
pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

done = False
clock = pygame.time.Clock()

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)

display_instructions = True
instruction_page = 1


def menyn():
    text = font.render("Play", True, WHITE)
    screen.blit(text, [10, 10])
    text = font.render("Highscore", True, WHITE)
    screen.blit(text, [10, 40])
    text = font.render("Quit", True, WHITE)
    screen.blit(text, [10, 40])


def meny_markör():


while not done:
    while not display_instructions:
        for event in pygame.event.get():
            # Gör att programet stängs när man trycker på en knapp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_DOWN:
                    instruction_page += 1
                if event.key == pygame.K_UP:
                    instruction_page -= 1
                if event.key == pygame.K_KP_ENTER:
                    if instruction_page == 1:
                        display_instructions = False
                    if instruction_page == 2:
                        print("Something")
                    if instruction_page == 3:
                        done = True
                else:
                    continue
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1

        # Färgen som fyller hela fönstret
        screen.fill(NIGHTBLUE)

        if instruction_page == 1:
            # Draw instructions, page 1
            # This could also load an image created in another program.
            # That could be both easier and more flexible.

            text = font.render("", True, WHITE)
            screen.blit(text, [10, 10])

            text = font.render("Page 1", True, WHITE)
            screen.blit(text, [10, 40])

        if instruction_page == 2:
            # Draw instructions, page 2
            text = font.render("This program bounces a rectangle", True, WHITE)
            screen.blit(text, [10, 10])

            text = font.render("Page 2", True, WHITE)
            screen.blit(text, [10, 40])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


pygame.quit()
