__author__ = 'ab53995'


def öppna_meny(screen):
    import pygame
    WHITE     = ( 255, 255, 255)
    NIGHTBLUE = (   0,   1,  64)

    # This is a font we use to draw text on the screen (size 36)
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()
    done_meny = False
    done = False

    def menyn():
        text = font.render("Play", True, WHITE)
        screen.blit(text, [200, 300])
        text = font.render("Highscore", True, WHITE)
        screen.blit(text, [200, 400])
        text = font.render("Help", True, WHITE)
        screen.blit(text, [200, 500])
        text = font.render("Quit", True, WHITE)
        screen.blit(text, [200, 600])

    class meny_markör():
        def __init__(self):
            self.markör_y = 400

        def rita(self, markör_y):
            pygame.draw.rect(screen, WHITE, [150, markör_y, 30, 30])

        def rörelse(self, markör_y):
            if event.key == pygame.K_DOWN:
                    markör_y += 100
            elif event.key == pygame.K_UP:
                    markör_y -= 100
            return markör_y

    """
    def meny_markör(markör_y):
        pygame.draw.rect(screen, WHITE, [150, markör_y, 30, 30])
    def meny_markör_rörelse(markör_y):
        if event.key == pygame.K_DOWN:
                markör_y += 100
        elif event.key == pygame.K_UP:
                markör_y -= 100
        return markör_y
    """
    markör = meny_markör

    while not done:
        for event in pygame.event.get():
            # Gör att programet stängs när man trycker på en knapp
            if event.type == pygame.KEYDOWN:
                """markör_y = meny_markör_rörelse(markör_y)"""

                if event.key == pygame.K_ESCAPE:
                    done = True
                    done_meny = True
                    break

                if event.key == pygame.K_RETURN:
                    if markör.markör_y == 300:
                        done = True
                    elif markör.markör_y == 400:
                        print("Something")
                    elif markör.markör_y == 600:
                        done = True
                        done_meny = True
                        break
                else:
                    continue

            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done = True
                done_meny = True
                break

        # Färgen som fyller hela fönstret
        screen.fill(NIGHTBLUE)

        menyn()

        meny_markör(markör_y)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    return(done_meny)

