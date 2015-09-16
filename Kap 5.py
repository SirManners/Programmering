
# Name:        Camel
# Purpose:
#
# Author:      ab53995, Jonas Cederberg
#
# Created:     04-09-2015
# Copyright:   (c) ab53995 2015
# Licence:     <your licence>

from math import *
import random
import pygame
clouds = """
              .

              |
     .               /
      \       I
                  /
        \  ,g88R_
          d888(`  ).                   _
 -  --==  888(     ).=--           .-(`  )`.
)         Y8P(       '`.          :(   .    )
        .+(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .=(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.+(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.



"""
camel = """
                    ,.
        .          :%%%.    .%%%.
   __%%%(\        `%%%%%   .%%%%%
 /a  ^  '%        %%%% %: ,%  %%"`
'__..  ,'%     .-%:     %-'    %
 ~~""%:. `     % '          .   `.
     %% % `   %%           .%:  . \.
      %%:. `-'   `        .%% . %: :\\
      %(%,%..."   `%,     %%'   %% ) )
       %)%%)%%'   )%%%.....- '   "/ (
       %a:f%%\ % / \`%  "%%% `   / \))
        %(%'  % /-. \      '  \ |-. '.
        `'    |%   `()         \|  `()
              ||    /          ()   /
              ()   0            |  o
               \  /\            o /
               o  `            /-|
            ,-/ `           ,-/

"""

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BROWN    = ( 77,   18,  18)
YELLOW   = ( 255, 251,   0)
BLUE     = (   0,   4, 255)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
# pygame.display.set_caption("Namn på fönster")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            done = True
        if event.type == pygame.QUIT:
            print("User has asked to quit.")
            done = True
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User has pressed a mousebutton.")

    # Game logic

    # Drawing



    screen.fill(YELLOW)

    pygame.draw.rect(screen, BLUE, [0, 0, 700, 200], 0)

    font = pygame.font.SysFont('Courier New', 10, False, False)
    i = 0
    # ökningen på i = typsnittets storlek ifall du vill att det ska se fint ut
    for line in camel.split("\n"):
        # \n står för att den ska göra en ny rad vid varje radbyte i orginaltexten,
        # ifall \n vore mellanslag skulle den göra en ny rad vid varje mellanslag
        text = font.render(line, True, BLACK)
        screen.blit(text, [200, 200+i])
        i += 10

    font = pygame.font.SysFont('Courier New', 40, False, False)
    text = font.render("YOU ARE WINNER", True, BLACK)
    screen.blit(text, [300, 400])

    font = pygame.font.SysFont('Courier New', 10, False, False)
    i = 0
    for line in clouds.split("\n"):
        text = font.render(line, True, BLACK)
        screen.blit(text, [0, 0+i])
        i += 10



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""
for x_offset in range(0, 700, 50):
        pygame.draw.line(screen, BLACK, [0+x_offset, 0], [0+x_offset, 500], 1)
    for y_offset in range(0, 700, 50):
        pygame.draw.line(screen, BLACK, [0, 0+y_offset], [700, 0+y_offset], 1)
    for x_offset in range(0, 700, 100):
        pygame.draw.line(screen, BLACK, [0+x_offset, 0], [0+x_offset, 500], 2)
    for y_offset in range(0, 700, 100):
        pygame.draw.line(screen, BLACK, [0, 0+y_offset], [700, 0+y_offset], 2)

    pygame.draw.polygon(screen, BLACK, [[350, 100], [250, 350], [450, 350]], 5)
    pygame.draw.ellipse(screen, BLACK, [200, 100, 300, 300], 10)

"""
# for y_offset in range(0, 500, 10):
#        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
# text = font.render(camel, True, BLACK)
#    screen.blit(text, [0, 0])
#    for i in range(200):

#        radians_x = i / 20
#        radians_y = i / 6

#        x = int( 75 * sin(radians_x)) + 200
#        y = int( 75 * cos(radians_y)) + 200

#    for x_offset in range(30,100, 30):
#        pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
#        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset-10, 100], 2)
#        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)
