import sprites
import pygame
import graphics

ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY, SCREEN_HEIGHT, SCREEN_WIDTH = graphics.färger()

def öppna_intro():

    # Objekt och data
    ridå = sprites.Ridå()
    ridå.x = 0
    ridå.y = -500
    ridå.bredd = 1366
    ridå.höjd = 1268
    ridå.change_y = 3
    ridå.färg = WHITE

"""
    # spelnamn = sprites.Text()
    # spelnamn.text = "RYMDSPEL"
    # spelnamn.x = 200
    # spelnamn.y = 300
    # spelnamn.colour = BLACK
    # spelnamn.font = 100

    done = False
    clock = pygame.time.Clock()
    parameter = 0

    # Main loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done = True

        screen.fill(NIGHTBLUE)

        spelnamn.skriv(screen)

        ridå.rita(screen)
        ridå.rörelse()

        pygame.display.flip()
        clock.tick(60)
"""

