__author__ = 'ab53995'

# Färger, http://www.colorpicker.com/
BLACK = (0, 0, 0)
ROSA    = ( 255, 0, 132)

import pygame
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
# För att få fullscreen, siffrorna är skärmens upplösning
pygame.display.set_mode((1366,768),pygame.FULLSCREEN)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        # Gör att programet stängs när man trycker på en knapp
        if event.type == pygame.KEYDOWN:
            done = True
        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True

    # Färgen som fyller hela fönstret
    screen.fill(ROSA)

    # Själva texten, siffran efter typsnittet är storleken
    font = pygame.font.SysFont('Courier New', 300, True, False)
    text = font.render("QUIZ!", True, BLACK)
    # Var på skärmen texten läggs ut
    screen.blit(text, [250, 200])

    # Printar allting på skärmen
    pygame.display.flip()
    # Hur många gånger per sekund som skärmen uppdateras
    clock.tick(60)

pygame.quit()
