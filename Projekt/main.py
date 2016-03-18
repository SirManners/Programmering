import pygame
import Meny
import sprites
import game

# --- Globala konstanter ---
NIGHTBLUE = (   0,   1,  64)
WHITE     = ( 255, 255, 255)

def main():

    # Pygame och fönster
    pygame.init()
    size = (1366, 688)
    screen = pygame.display.set_mode(size)
    # pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    pygame.display.set_caption("Projekt 1")

    # Objekt och data
    done = False
    done_game = True
    clock = pygame.time.Clock()
    resume = False
    session = game.Game()
    highscore = 0

    # Main loop
    # Intro.öppna_intro(screen)
    while not done:
        done = Meny.öppna_meny(screen, resume)
        if not done:
            done_game = False
        while not done_game:
            done_game = session.process_events()

            session.run_logic()
            if session.highscore > highscore:
                highscore = session.highscore
                print("Detta är den nya highscoren", highscore)
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