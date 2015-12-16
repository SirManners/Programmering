import pygame
import random
import Klasser
import math

# Klasser.färger()
SCREEN_HEIGHT = 688
SCREEN_WIDTH = 1366
ROSA = ( 255,   0, 132)
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


class Spelare(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2 - 15
        self.rect.y = 300
        self.move_x = 4
        self.move_y = 4
        self.player_up = False
        self.player_down = False
        self.player_left = False
        self.player_right = False

    def update(self):
        # tills vidare
        if self.player_up:
            self.rect.y -= self.move_y
        if self.player_down:
            self.rect.y += self.move_y
        if self.player_left:
            self.rect.x -= self.move_x
        if self.player_right:
            self.rect.x += self.move_x


class Fiendermall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.move_x = 2
        self.move_y = 1
        # self.remove_width
        # self.remove_height

    def reset_pos(self):
        self.rect.y = random.randrange(300, 500)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.rect.y += self.move_y
        self.rect.x += self.move_x
        # if 0 + self.rect.height > self.rect.x > SCREEN_WIDTH + self.rect.height:
        # ta bort
        # if 0 + self.rect.width > self.rect.y > SCREEN_HEIGHT + self.rect.height:
        # ta bort

"""
class Boss(pygame.sprite.Sprite, Fiendermall):
    def __init__(self):
        super().__init__()
        # pygame.sprite.Sprite.__init__()
        # Fiendermall.__init__()

    def död(self):
        Game.level += 1

        # HP bars? Mer komplicerade attacker?


class Grafik():
    def __init_(self):


"""

# class Projektil(pygame.sprite.Sprite):


class Game(object):

    def __init__(self):

        # Attributes
        self.level = 1
        self.score = 0
        self.game_over = False

        # Create sprites lists
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # self.projectile_list = pygame.sprite.Group()
        # self.all_sprites_list.add(self.projectile_list)

        self.player = Spelare()
        self.all_sprites_list.add(self.player)

        # Create the sprites
        # Projektiler, skapa ifall variabel?
        mobs = Fiendermall()
        mobs.image = pygame.Surface([20, 20])
        self.enemy_list.add(mobs)
        self.all_sprites_list.add(mobs)

        boss = Fiendermall()
        # Senare bossmall
        boss.image = pygame.Surface([200, 200])
        self.boss_list.add(boss)
        self.enemy_list.add(boss)
        self.all_sprites_list.add(boss)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.__init__()
                if event.key == pygame.K_1:
                    self.game_over = True
                if event.key == pygame.K_w:
                    self.player.player_up = True
                if event.key == pygame.K_s:
                    self.player.player_down = True
                if event.key == pygame.K_a:
                    self.player.player_left = True
                if event.key == pygame.K_d:
                    self.player.player_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.player_up = False
                if event.key == pygame.K_s:
                    self.player.player_down = False
                if event.key == pygame.K_a:
                    self.player.player_left = False
                if event.key == pygame.K_d:
                    self.player.player_right = False

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()
            # projectile_hit_list = pygame.sprite.spritecollide(self.projectile, self.enemy_list, True)
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)

            if len(enemy_hit_list) != 0:
                self.game_over = True

            for collision in enemy_hit_list:
                self.score += 1
                print(self.score)
            # for enemy in projectile_hit_list:
                # self.score += 1

    def display_frame(self, screen):
        if self.level == 1:
            screen.fill(NIGHTBLUE)
        if self.level == 2:
            screen.fill(RED)

        if self.game_over:
            print("you are rip")

            """ rip meddelande """

        if not self.game_over:
            self.all_sprites_list.draw(screen)
            # den ritar ingenting

        pygame.display.flip()