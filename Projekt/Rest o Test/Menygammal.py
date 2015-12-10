__author__ = 'ab53995'


def öppna_meny():
    import pygame
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

    clock = pygame.time.Clock()

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    display_instructions = False
    instruction_page = 1
    markör_y = 400

    def menyn():
        text = font.render("Play", True, WHITE)
        screen.blit(text, [200, 400])
        text = font.render("Highscore", True, WHITE)
        screen.blit(text, [200, 500])
        text = font.render("Quit", True, WHITE)
        screen.blit(text, [200, 600])

    def meny_markör(markör_y):
        pygame.draw.rect(screen, WHITE, [150, markör_y, 30, 30])

    while not display_instructions:
        for event in pygame.event.get():
            # Gör att programet stängs när man trycker på en knapp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    display_instructions = True
                elif event.key == pygame.K_DOWN:
                    instruction_page += 1
                    markör_y += 100
                elif event.key == pygame.K_UP:
                    instruction_page -= 1
                    markör_y -= 100
                elif event.key == pygame.K_RETURN:
                    if instruction_page == 1:
                        display_instructions = True
                    elif instruction_page == 2:
                        print("Something")
                    elif instruction_page == 3:
                        display_instructions = True
                else:
                    continue
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                display_instructions = True
                done = True
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1

        # Färgen som fyller hela fönstret
        screen.fill(NIGHTBLUE)

        menyn()

        meny_markör(markör_y)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()

öppna_meny()