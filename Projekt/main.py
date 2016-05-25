import pygame
import sprites
import game
import graphics

ROSA, \
BLACK, \
WHITE, \
GREEN, \
RED, \
BROWN, \
YELLOW, \
BLUE, \
NIGHTBLUE, \
STARBLUE, \
GREY, \
SCREEN_HEIGHT, \
SCREEN_WIDTH = \
    graphics.colour()


def main():

    ### Pygame and window size
    pygame.init()
    size = (1366, 688)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Projekt 1")

    ### Objects and data
    clock = pygame.time.Clock()
    done_game = False
    resume = False
    session = game.Game()
    highscore = 0
    pygame.mouse.set_visible(False)

    ### Main pygame loop
    while not done_game:

        done_game = session.process_events
        session.run_logic()

        if session.highscore > highscore:
            highscore = session.highscore
            session.highscore_message = True

        session.display_frame(screen, highscore)

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
