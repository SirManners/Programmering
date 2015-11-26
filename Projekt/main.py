import pygame
import Projekt.Meny
import Projekt.Intro
import Projekt.Klasser
"""import Programmering.Projekt.Meny
import Programmering.Projekt.Intro osv på skoldatorn"""

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
    done_game = False
    clock = pygame.time.Clock()
    resume = False

    # Main loop
    Projekt.Intro.öppna_intro(screen)
    while not done:
        done = Projekt.Meny.öppna_meny(screen, resume)
        if not done:
            done_game = False
        while not done_game:
            for event in pygame.event.get():
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

    pygame.quit()

if __name__ == "__main__":
    main()