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


# Latemanslösning, se grafik
snow_list = []
for i in range(50):
    snow_x = random.randrange(0, 1366)
    snow_y = random.randrange(-768, 0)
    snow_list.append([snow_x, snow_y])


def snow(screen):
    for i in range(len(snow_list)):
            pygame.draw.circle(screen, WHITE, snow_list[i], 2)
            snow_list[i][1] += 5
            if snow_list[i][1] > 768:
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                x = random.randrange(0, 1366)
                snow_list[i][0] = x

# Gör om så att både spelare och fiender båda är barn till samma klass?

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
        self.player_shoot = False

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
        # if self.player_shoot:
            #
# Hur ska jag få den att skjuta något med players x och y koord samtidigt som jag ritar något nytt?



class Fiendermall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.move_x = 2
        self.move_y = 2
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
class Projektil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3, 3])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.move_y = 30
        self.rect.x = self.player.rect.x
        self.rect.x = self.player.rect.x

    def update(self):
        # någonting görs true i en lista med alla projektiler när du klickar på shoot,
        # sätts false när de lämnar skärmen eller krockar.
        #

class Boss(pygame.sprite.Sprite, Fiendermall):
    def __init__(self):
        super().__init__()
        # pygame.sprite.Sprite.__init__()
        # Fiendermall.__init__()

    def död(self):
        Game.level += 1

        # HP bars? Mer komplicerade attacker?


class Grafik:
    def __init_(self):
        self.snow_list = []
        self.snow_x = 0
        self.snow_y = 0
        # fixa så att det inte bara är snö som är grafik

    def snö(self):
        for i in range(50):
            self.snow_x = random.randrange(0, 1366)
            self.snow_y = random.randrange(-768, 0)
            self.snow_list.append([self.snow_x, self.snow_y])

    def draw_snow(self, screen):
        for i in range(len(self.snow_list)):
            pygame.draw.circle(screen, WHITE, self.snow_list[i], 2)
            self.snow_list[i][1] += 1
            if self.snow_list[i][1] > 768:
                y = random.randrange(-50, -10)
                self.snow_list[i][1] = y
                x = random.randrange(0, 1366)
                self.snow_list[i][0] = x


class Stjärnor(Grafik):
    def __init__(self):
        super().__init__()

"""


class Game(object):

    def __init__(self):

        # Attributes
        self.player_hp = 3
        self.level = 1
        self.score = 0
        self.game_over = False
        # Grafik
        # stjärnor = Grafik
        # stjärnor.snö()
        # Create sprites lists
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        self.player = Spelare()
        self.player_list.add(self.player)
        self.all_sprites_list.add(self.player)

        # Create the sprites
        # Projektiler, skapa ifall variabel?

        # Level 1:
        if self.level == 1:
            # detta fungerar dock inte
            mobs = Fiendermall()
            mobs.image = pygame.Surface([20, 20])
            self.enemy_list.add(mobs)
            self.all_sprites_list.add(mobs)

            boss = Fiendermall()
            # Senare bossmall
            boss.image = pygame.Surface([200, 200])
            # ha den i update funk för att gå i kurva
            boss.rect.y = 200 + 100*math.sin(math.radians(boss.rect.x))
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
                if event.key == pygame.K_x:
                    self.player.player_shoot = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.player_up = False
                if event.key == pygame.K_s:
                    self.player.player_down = False
                if event.key == pygame.K_a:
                    self.player.player_left = False
                if event.key == pygame.K_d:
                    self.player.player_right = False
                if event.key == pygame.K_x:
                    self.player.player_shoot = False


    def run_logic(self):
        self.enemy_list.update()
        if not self.game_over:
            self.player.update()

            # projectile_hit_list = pygame.sprite.spritecollide(self.projectile, self.enemy_list, True)
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)

            if len(enemy_hit_list) != 0:
                self.player_hp -= 1

            if self.player_hp == 0:
                self.game_over = True

            for collision in enemy_hit_list:
                self.score += 1
                print(self.score)
            # for enemy in projectile_hit_list:
                # self.score += 1

    def display_frame(self, screen):
        if self.level == 1:
            screen.fill(NIGHTBLUE)
            snow(screen)
            # Grafik.draw_snow(screen)
        if self.level == 2:
            screen.fill(RED)

        if self.game_over:
            print("you are rip")

            """ rip meddelande """
        self.enemy_list.draw(screen)
        # Ha olika enemy_lists för olika nivåer. briljant jonas, briljant
        self.projectile_list.draw(screen)
        if not self.game_over:
            self.player_list.draw(screen)
            # fixa så den ritar fienderna efter du dött

        pygame.display.flip()