
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

print(r""" _    _      _
| |  | |    | |
| |  | | ___| | ___ ___  _ __ ___   ___
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \
\  /\  /  __/ | (_| (_) | | | | | |  __/
 _/  \/ \__________\___/|_| |_| |_|\____
| |        /  __ \                    | |
| |_ ___   | /  \/ __ _ _ __ ___   ___| |
| __/ _ \  | |    / _` | '_ ` _ \ / _ \ |
| || (_) | | \__/\ (_| | | | | | |  __/ |
 \__\___/   \____/\__,_|_| |_| |_|\___|_|""")
print("\nYou have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives.\n")

# i = avståndet du har gått
# j = avståndet natives har gått

drinks = 3
fatigue = 1
thirst = 0
i = 20
j = 0
k = 0
goal = 220
day = 1

movement = ("b", "c")

print("***** Day", day, (" *****"))
while i < goal and j <= i and thirst <= 6:
    print("A. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. ")
    print("D. Stop and rest. \nE. Status check. \nQ. Quit. \n")
    answer = input("Your choice? \n").lower()

    if answer == "q":
        j += 50000
        break

    if answer == "a":
        if drinks < 1:
            print("You have no drinks left")
            continue
        else:
            fatigue += 0.5
            drinks -= 1
            print("You drink some water and recoved some fatigue. You have", drinks, " drink(s) left\n")
            j += random.randrange(7, 14)
            thirst = 0
            day += 1

    if answer == "b":
        if fatigue <= 0.35:
            print("You are too tired to run")
            continue
        else:
            k = random.randrange(5, 12) * fatigue
            i += k
            fatigue -= 0.2
            j += random.randrange(7, 14)
            print("You move at a moderate speed and cover", k, "miles\n")
            thirst += 1
            day += 1


    if answer == "c":
        if fatigue <= 0.35:
            print("You are too tired to run")
            continue
        else:
            k = random.randrange(10, 21) * fatigue
            i += k
            fatigue -= 0.5
            j += random.randrange(7, 14)
            print("You do a quick march and cover", k, "miles\n")
            thirst += 1
            day += 1


    if answer == "d":
        fatigue += 1.0
        j += random.randrange(10, 14)
        print("You rest for the day and recover fatigue\n")
        day += 1


    if answer == "e":
        print("Miles traveled:", i - 20, "\nYou got ", drinks, " left\nThe natives are", i-j, "miles behind you.")
        continue

    oasis = random.randrange(1, 16)

    if oasis == 5 and answer in movement:
        print("You found an oasis!")
        fatigue += 0.9
        thirst = 0
        drinks += 1

    print("***** Day ", day, " *****")

    if (i-j) < 15 and (i-j) > 0 and i < goal:
        print("*The natives are getting close!*")

    if thirst >= 4 and (i-j) >= 0 and i < goal:
            print("*You are very dehydrated, drink or risk dying!*")

    if i < goal:
        print("Miles traveled:", i - 20, "\nYou got ", drinks, " drinks left\nThe natives are", i-j, "miles behind you.")

# Slut:
if i > j and thirst <= 6:
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Kapitel 5")
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done = True

        screen.fill(YELLOW)

        pygame.draw.rect(screen, BLUE, [0, 0, 700, 200], 0)

        font = pygame.font.SysFont('Courier New', 10, True, False)
        i = 0
        for line in camel.split("\n"):
            text = font.render(line, True, BLACK)
            screen.blit(text, [200, 200+i])
            i += 10

        font = pygame.font.SysFont('Courier New', 40, False, False)
        text = font.render("YOU ARE WINNER", True, BLACK)
        screen.blit(text, [300, 400])

        font = pygame.font.SysFont('Courier New', 10, True, False)
        i = 0
        for line in clouds.split("\n"):
            text = font.render(line, True, WHITE)
            screen.blit(text, [0, 0+i])
            i += 10



        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

else:

    if (j - i) > 40000:
        print("\nCoward")

    elif thirst >= 6:
        print("You died of dehydration, the natives found your corpse and got back their camel.")

    elif oasis == 5:
        print("You hid from the natives in the oasis!")
        print("Foolishly they ran past you, and never suspected a thing.")
        print("After a long rest you and your camel went back from whence you came and together you lived happily ever after.")

    elif j > i:
        print("The natives caught you and took back their camel. You were put to the sword the next morning.")

print()
