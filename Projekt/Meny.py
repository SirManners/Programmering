import pygame
import sprites
import game
import main
import graphics

ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY, SCREEN_HEIGHT, SCREEN_WIDTH = graphics.färger()



def öppna_meny(screen, resume):

    def menyn(screen):
        font = pygame.font.SysFont("system bold", 36)
        text = font.render("Highscore", True, WHITE)
        screen.blit(text, [200, 400])
        text = font.render("Help", True, WHITE)
        screen.blit(text, [200, 500])
        text = font.render("Quit", True, WHITE)
        screen.blit(text, [200, 600])
        if resume is False:
            text = font.render("Play", True, WHITE)
            screen.blit(text, [200, 300])

        else:
            text = font.render("Resume", True, WHITE)
            screen.blit(text, [200, 300])
    # gör om till ett resultat av Text klassen, flytta ut ur öppna_meny
    # spara text utanför loopen
    # Gör en lista och kör igenom den och rita allting

    class Markör(graphics.Rektangel):
        def __init__(self):
            super().__init__()

        def rörelse(self):
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if self.y < 600:
                    self.y += self.change_y
                else:
                    self.y = 300
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if self.y > 300:
                    self.y -= self.change_y
                else:
                    self.y = 600

    #Objekt och data

    meny_markör = Markör()
    meny_markör.bredd = 30
    meny_markör.höjd = 30
    meny_markör.x = 150
    meny_markör.y = 300
    meny_markör.change_y = 100

    clock = pygame.time.Clock()
    done_meny = False
    done = False

    # Main loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                meny_markör.rörelse()
                if event.key == pygame.K_ESCAPE:
                    done = True
                    done_meny = True

                if event.key == pygame.K_RETURN:
                    if meny_markör.y == 300:
                        done = True
                    elif meny_markör.y == 400:
                        font = pygame.font.SysFont("system bold", 36)
                        text = font.render("Your highscore is ", True, WHITE)
                        screen.blit(text, [200, 300])
                        #highscore.text = "Your highscore is ", main.highscore
                        # Fixa så att all annan text försvinner
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

        screen.fill(NIGHTBLUE)

        menyn(screen)

        meny_markör.rita(screen)

        clock.tick(60)

        pygame.display.flip()
    resume = True
    return(done_meny)

