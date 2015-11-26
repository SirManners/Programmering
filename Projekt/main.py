import pygame
"""import Programmering.Projekt.Meny
import Programmering.Projekt.Intro osv på skoldatorn"""
import Projekt.Meny
import Projekt.Intro
import Projekt.Klasser

__author__ = 'ab53995'
# Färger, http://www.colorpicker.com/

NIGHTBLUE = (   0,   1,  64)
WHITE     = ( 255, 255, 255)


pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
# För att få fullscreen, siffrorna är skärmens upplösning
pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

done = False
done_game = False
clock = pygame.time.Clock()
resume = False
Projekt.Intro.öppna_intro(screen)

while not done:
    done = Projekt.Meny.öppna_meny(screen, resume)
    if not done:
        done_game = False
    while not done_game:
        for event in pygame.event.get():
            # Gör att programet stängs när man trycker på en knapp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done_game = True
                    # resume = True
                    # gör så att man får upp en resumeknapp
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done_game = True

        # Färgen som fyller hela fönstret
        screen.fill(NIGHTBLUE)
        pygame.draw.rect(screen, WHITE, [100, 100, 50, 200])
        # Printar allting på skärmen
        pygame.display.flip()
        # Hur många gånger per sekund som skärmen uppdateras
        clock.tick(60)

pygame.quit()
