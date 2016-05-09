import pygame
import Meny
import sprites
import game
import graphics

ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY, SCREEN_HEIGHT, SCREEN_WIDTH = graphics.färger()


def main():

    # Pygame och fönster
    pygame.init()
    size = (1366, 688)
    screen = pygame.display.set_mode(size)
    # pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    pygame.display.set_caption("Projekt 1")

    # Objekt och data

    clock = pygame.time.Clock()

    done_meny = False
    done_game = True
    resume = False
    session = game.Game()

    highscore = 0

    # Main loop
    # Intro.öppna_intro(screen)
    while not done_meny:
        done_meny = Meny.öppna_meny(screen, resume)
        if not done_meny:
            done_game = False
            passed_time = pygame.time.get_ticks()
        while not done_game:
            done_game = session.process_events #(passed_time) #doesn't work for some reason

            session.run_logic()

            if session.highscore > highscore:
                highscore = session.highscore
                session.highscore_message = True

            session.display_frame(screen)

            clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()


"""    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done_game = True
                        # resume = True
                        # gör så att man får upp en resumeknapp
                if event.type == pygame.QUIT:
                    print("User has asked to quit.")
                    done_game = True

            screen.fill(NIGHTBLUE)
            pygame.draw.rect(screen, WHITE, [100, 100, 50, 200])

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()"""