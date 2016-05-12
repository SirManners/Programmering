import sprites
import trig
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
STARBLUE, GREY, \
SCREEN_HEIGHT, \
SCREEN_WIDTH = \
    graphics.colour()


class Level():
    def __init__(self):
        self.level = 0
        self.enemy_count = 0
        self.enemy_colour = BLACK
        self.level_background = NIGHTBLUE

    def set_level(self, screen):
        screen.fill(self.level_background)

    def create_enemies(self, name):
        name = sprites.Enemies()


        """

# Level 1
if self.level == 1:
    # create sprites of level one, add them to all_sprites.
    # create function that creates levels of sprites
    if len(self.enemy_list1) == 0:
        if self.boss1.active == 0:
            print("Boss has spawned")
            if self.boss1.active ==0:
                self.boss1.active += 1
        self.boss_list1.update()
        if self.boss1.hp < 1:
            self.level += 1
            self.boss_list.remove(self.boss1)
        else:
            #print("Cap?", self.cap)
            #print(self.boss1.projectile_number)

            if self.boss1.projectile_number < 50 and not self.cap: # use sinus instead?
                self.boss1.projectile_number += 1
                self.boss_projectile = sprites.Bossprojectile()
                self.boss1.shoot(1, self.boss_projectile, self.all_sprites_list, self.projectile_list, self.player.rect.x, self.player.rect.y)
            else:
                self.cap = True
                if self.boss1.projectile_number > 1:
                    self.boss1.projectile_number -= 1
                else:
                    self.cap = False
    else:
        # self.enemy_list1.choose_target(self.player.rect.x, self.player.rect.y)
        self.enemy_list1.update()


# Level 2
if self.level == 2:
    if len(self.enemy_list2) == 0:
        if self.boss2.active == 0:
            print("Boss has spawned")
            self.boss2.active += 1
        self.boss_list2.update()
        if self.boss2.hp < 1:
            self.level += 1
            self.boss_list.remove(self.boss2)
    else:
        self.enemy_list2.update()

# Level 3
"""