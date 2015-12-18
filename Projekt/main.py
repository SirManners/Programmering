import pygame
import Meny
import Intro
import Klasser
import Spel

# --- Globala konstanter ---
NIGHTBLUE = (   0,   1,  64)
WHITE     = ( 255, 255, 255)

# --- Klasser ---


def main():

    # Pygame och fönster
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    pygame.display.set_caption("Projekt 1")

    # Objekt och data
    done = False
    done_game = True
    clock = pygame.time.Clock()
    resume = False
    # spel = Spel.Game()
    game = Spel.Game()


    # Main loop
    # Intro.öppna_intro(screen)
    while not done:
        done = Meny.öppna_meny(screen, resume)
        if not done:
            done_game = False
        while not done_game:
            done_game = game.process_events()

            enemy_hit_list = game.run_logic()

            game.display_frame(screen)

            clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

"""


if __name__ == "__main__":
    main()
 """

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