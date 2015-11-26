__author__ = 'ab53995'


def öppna_meny(screen, resume):
    import pygame
    import Projekt.Klasser

    def menyn():
        if resume is False:
            text = font.render("Play", True, WHITE)
            screen.blit(text, [200, 300])
            text = font.render("Highscore", True, WHITE)
            screen.blit(text, [200, 400])
            text = font.render("Help", True, WHITE)
            screen.blit(text, [200, 500])
            text = font.render("Quit", True, WHITE)
            screen.blit(text, [200, 600])
        else:
            text = font.render("Resume", True, WHITE)
            screen.blit(text, [200, 300])
            text = font.render("Highscore", True, WHITE)
            screen.blit(text, [200, 400])
            text = font.render("Help", True, WHITE)
            screen.blit(text, [200, 500])
            text = font.render("Quit", True, WHITE)
            screen.blit(text, [200, 600])

    class Markör(Projekt.Klasser.Rektangel):
        def __init__(self):
            super().__init__()

        def rörelse(self):
            if event.key == pygame.K_DOWN:
                if self.y < 600:
                    self.y += self.change_y
                else:
                    self.y = 300
            elif event.key == pygame.K_UP:
                if self.y > 300:
                    self.y -= self.change_y
                else:
                    self.y = 600

    # This is a font we use to draw text on the screen (size 36)
    WHITE     = ( 255, 255, 255)
    NIGHTBLUE = (   0,   1,  64)

    clock = pygame.time.Clock()
    done_meny = False
    done = False

    font = pygame.font.Font(None, 36)
    meny_markör = Markör()
    meny_markör.bredd = 30
    meny_markör.höjd = 30
    meny_markör.x = 150
    meny_markör.y = 300
    meny_markör.change_y = 100

    while not done:
        for event in pygame.event.get():
            # Gör att programet stängs när man trycker på en knapp
            if event.type == pygame.KEYDOWN:
                meny_markör.rörelse()
                if event.key == pygame.K_ESCAPE:
                    done = True
                    done_meny = True

                if event.key == pygame.K_RETURN:
                    if meny_markör.y == 300:
                        done = True
                    elif meny_markör.y == 400:
                        print("Something")
                    elif meny_markör.y == 600:
                        done = True
                        done_meny = True
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

        meny_markör.rita(screen)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    resume = True
    return(done_meny)

