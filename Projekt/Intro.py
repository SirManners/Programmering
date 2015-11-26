

def öppna_intro(screen):

    import pygame
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

    def introskärm():
        ridå_x = 0
        ridå_y = 0
        pygame.draw.rect(screen, WHITE, [ridå_x, ridå_y, 50, 200])

    done = False
    clock = pygame.time.Clock()
    parameter = 0
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

        introskärm()

        # Printar allting på skärmen
        pygame.display.flip()
        # Hur många gånger per sekund som skärmen uppdateras
        clock.tick(60)
        """parameter += 1
        if parameter == 4:
            done = True
        else:
            continue"""

