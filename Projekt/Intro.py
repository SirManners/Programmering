import Klasser
import pygame

# --- Globala konstanter ---
NIGHTBLUE = (   0,   1,  64)
WHITE     = ( 255, 255, 255)
RED       = ( 255,   0,   0)
STARBLUE  = ( 159, 161, 252)
BLACK     = (   0,   0,   0)

# --- Klasser ---




def öppna_intro():

    # Objekt och data
    ridå = Klasser.Ridå()
    ridå.x = 0
    ridå.y = -500
    ridå.bredd = 1366
    ridå.höjd = 1268
    ridå.change_y = 3
    ridå.färg = WHITE

"""
    # spelnamn = Klasser.Text()
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

