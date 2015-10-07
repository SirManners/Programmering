__author__ = 'ab53995'

import random
import pygame

BLACK     = (   0,   0,   0)
WHITE     = ( 255, 255, 255)
GREEN     = (   0, 255,   0)
RED       = ( 255,   0,   0)
BROWN     = (  77,  18,  18)
YELLOW    = ( 255, 251,   0)
BLUE      = (   0,   4, 255)
NIGHTBLUE = (   0,   1,  64)
STARBLUE  = ( 159, 161, 252)
GREY      = (  50,  50,  82)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
"""

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kapitel 5")
"""



snow_list = []
for i in range(50):
    x = random.randrange(0, 1366)
    y = random.randrange(-768, 0)
    snow_list.append([x, y])

projectile_list = []

done = False
clock = pygame.time.Clock()

rekt_x1 = 0
rekt_y1 = 300

rekt_x2 = 50
rekt_y2 = 50

rekt_change_x1 = 5
rekt_change_y1 = 5

rekt_change_x2 = 5
rekt_change_y2 = 5

x_mouse = 0
y_mouse = 0

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 600
projectile_speed = 5

x_total = 0
y_total = 0

time1 = 0
time2 = 0
time_down = pygame.time.get_ticks()
acc = 0
keydown = [None, False, False, False, False]

x_shoot = -1
y_shoot = -1
death = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

def rektangel(x, y, speed_x, speed_y):
    pygame.draw.rect(screen, WHITE, [x, y, 50, 50])
    pygame.draw.rect(screen, RED, [x + 10, y + 10, 30, 30])
    x += speed_x
    y += speed_y
    if x > 1316 or x < 0:
        speed_x *= -1
    if y > 718 or y < 0:
        speed_y *= -1

kanter = "x_coord", "y_coord"

while not done:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            time1 = pygame.time.get_ticks()
            if event.key == pygame.K_w:
                y_speed = -2
                keydown[1] = True
            if event.key == pygame.K_s:
                y_speed = 2
                keydown[2] = True
            if event.key == pygame.K_a:
                x_speed = -2
                keydown[3] = True
            if event.key == pygame.K_d:
                x_speed = 2
                keydown[4] = True
            if event.key == pygame.K_ESCAPE:
                done = True

            if event.key == pygame.K_x:
                time3 = pygame.time.get_ticks()
                keydown[0] = True
                x_shoot = x_coord
                y_shoot = y_coord


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w:
                keydown[1] = False
                if keydown[2] == False and keydown[3] == False and keydown[4] == False:
                    y_speed = 0
                    x_speed = 0

            if event.key == pygame.K_s:
                keydown[2] = False
                if keydown[1] == False and keydown[3] == False and keydown[4] == False:
                    y_speed = 0
                    x_speed = 0

            if event.key == pygame.K_a:
                keydown[3] = False
                if keydown[1] == False and keydown[2] == False and keydown[4]== False:
                    x_speed = 0
                    y_speed = 0
            if event.key == pygame.K_d:
                keydown[4] = False
                if keydown[2] == False and keydown[3] == False and keydown[1] == False:
                    x_speed = 0
                    y_speed = 0

            if event.key == pygame.K_ESCAPE:
                done = True

            if event.key == pygame.K_x:
                keydown[0] = False
                time4 = pygame.time.get_ticks() - time3
        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            x_mouse = pos[0]
            y_mouse = pos[1]
            # gör så att man skjuter emot mouse_pos

# Game logic

    if keydown[1] or keydown[2] or keydown[3] or keydown[4]:
        time2 = pygame.time.get_ticks() - time1
        print(time2/1000)
        acc = 0.5 * time2/1000
        if keydown[1]:
            y_speed -= acc
        if keydown[2]:
            y_speed += acc
        if keydown[3]:
            x_speed -= acc
        if keydown[4]:
            x_speed += acc

        if not keydown[0]:
            x_shoot = 0
            y_shoot = 0

    y_shoot -= projectile_speed

    x_coord += x_speed
    y_coord += y_speed

    if x_coord - rekt_x1 in death and y_coord - rekt_y1 in death:
        print("Game over")
        keydown[0] = True
    # lägg till något som dödar dig

    if x_coord > 1351 or x_coord < 0:
        x_speed *= -1

    if y_coord > 753 or y_coord < 0:
        y_speed *= -1

    # kollision med kanten

    # if kanter

    screen.fill(NIGHTBLUE)

# Grafik

    rektangel(50, 50, 5, 5)

    rektangel(0, 300, 5, 5)

    pygame.draw.rect(screen, WHITE, [rekt_x2, rekt_y2, 50, 50])
    pygame.draw.rect(screen, RED, [rekt_x2 + 10, rekt_y2 + 10, 30, 30])
    rekt_x2 += rekt_change_x2
    rekt_y2 += rekt_change_y2
    if rekt_x2 > 1316 or rekt_x2 < 0:
        rekt_change_x2 *= -1
    if rekt_y2 > 718 or rekt_y2 < 0:
        rekt_change_y2 *= -1

    pygame.draw.rect(screen, BLACK, [x_coord, y_coord, 15, 15])

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 768:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 1366)
            snow_list[i][0] = x

    if keydown[0] or y_shoot < 768:
        pygame.draw.rect(screen, YELLOW, [x_shoot + 3, y_shoot + 5, 5, 5])




        # gör att projektilerna fungerar som snöflingorna? listor och så?






    pygame.display.flip()

    clock.tick(120)

pygame.quit()

"""if keydown[0]:
        font = pygame.font.SysFont('Courier New', 300, True, False)
        text = font.render("GAME OVER!", True, BLACK)
        screen.blit(text, [250, 200])


# detta funerar ej :/
if keydown[0]:
        for i in range[0, 10]:
            x_1 = x_shoot
            y_1 = y_shoot
            projectile_list.append([x_1, y_1])
        for i in range(len(projectile_list)):
            pygame.draw.circle(screen, YELLOW, projectile_list[i], 2)
        projectile_list[i][1] += 1
        if projectile_list[i][1] > 768:
            y = random.randrange(-50, -10)
            projectile_list[i][1] = y
            x = random.randrange(0, 1366)
            projectile_list[i][0] = x
"""