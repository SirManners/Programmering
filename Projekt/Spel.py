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
            # fixa så att stjärnorna åker snabbare när man åker uppåt, och långsammare när man åker nedåt
            if snow_list[i][1] > 768:
                y = random.randrange(-50, -10)
                snow_list[i][1] = y
                x = random.randrange(0, 1366)
                snow_list[i][0] = x

# Gör om så att både spelare och fiender båda är barn till samma klass?



class Game(object):

    def __init__(self):

        # Attributes
        self.player_hp = 10
        self.level = 1
        # Lägg till lvl -1 som är introskärm, lvl 0 som är meny??
        self.score = 0
        self.highscore = 0
        self.game_over = False

        # Grafik
        # HP markörer
        # stjärnor = Grafik
        # stjärnor.snö()
        # när du fixat snön på riktigt. Ha planeter i bakrunden annars?

        # Create sprites lists
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        # Gör en loop som skapar listorna?
        self.boss_list1 = pygame.sprite.Group()
        self.boss_list2 = pygame.sprite.Group()
        self.enemy_list1 = pygame.sprite.Group()
        self.enemy_list2 = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        # Spelare
        self.player = Klasser.Spelare()
        self.player_list.add(self.player)
        self.all_sprites_list.add(self.player)

        # Projektiler:
        """
        for x in range(10):
            player_projektil = Klasser.Projektil()
            self.all_sprites_list.add(player_projektil)
            self.projectile_list.add(player_projektil)
"""
        # Create the sprites

        # Level 1:
        for  x in range(10):
            mobs1 = Klasser.Fiendermall()
            mobs1.rect.x = random.randrange(40, SCREEN_WIDTH - 40)
            mobs1.rect.y = random.randrange(-500, -300)
            mobs1.move_x = 0
            mobs1.move_y = 3
            self.enemy_list.add(mobs1)
            self.enemy_list1.add(mobs1)
            self.all_sprites_list.add(mobs1)

        boss1 = Klasser.Fiendermall()
        # Senare bossmall, typ boss1 = Bossmall()

        boss1.image = pygame.Surface([200, 200])
        boss1.rect = boss1.image.get_rect()
        boss1.rect.x = SCREEN_WIDTH / 2 - boss1.image.get_width()
        boss1.rect.y = -200
        boss1.move_x = 0
        boss1.move_y = 4
        # ha den i update funk för att gå i kurva
        #boss1.rect.y = 200 + 100*math.sin(math.radians(boss.rect.x))

        self.boss_list.add(boss1)
        self.boss_list1.add(boss1)
        self.all_sprites_list.add(boss1)

        # Level 2:
        i = 0
        for x in range(20):
            mobs2 = Klasser.Fiendermall()
            mobs2.rect.x = 40 + i
            mobs2.rect.y = random.randrange(-200, 0)
            mobs2.move_x = 0
            mobs2.move_y = 3
            self.enemy_list.add(mobs2)
            self.enemy_list2.add(mobs2)
            self.all_sprites_list.add(mobs2)
            i += 80

        boss2 = Klasser.Fiendermall()
        boss2.image = pygame.Surface([500,500])
        boss2.rect = boss2.image.get_rect()
        boss2.rect.x = SCREEN_WIDTH /2 - boss2.image.get_width()
        boss2.rect.y = -1000
        self.boss_list.add(boss2)
        self.boss_list2.add(boss2)
        self.all_sprites_list.add(boss2)

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

            print("Nivå:", self.level)
            print("Score:", self.score)
            print("Hitpoints", self.player_hp)
            print("Highscore", self.highscore)
            print("--------------------------")
            # projectile_hit_list = pygame.sprite.spritecollide(self.projectile, self.enemy_list, True)
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
            boss_hit_list = pygame.sprite.spritecollide(self.player, self.boss_list, True)

            if not self.game_over:
                self.player.update()
            if self.game_over:
                if self.score > self.highscore:
                    self.highscore = self.score
                self.score = 0
                print("rip")
            # Gör en loop (eller funktion) istället, som tar self.level och gör detta med den
            # Level 1
            if self.level == 1:
                self.enemy_list1.update()
                if self.score > 2:
                    self.boss_list1.update()
            # Level 2
            if self.level == 2:
                self.enemy_list2.update()
                if self.score > 3:
                    self.boss_list2.update()

            for collision in boss_hit_list:
                self.level += 1

            if self.player_hp < 1:
                self.game_over = True

            for collision in enemy_hit_list:
                self.score += 1
                self.player_hp -= 1
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
            snow(screen)

            """ rip meddelande """

        if self.level == 1:
            self.enemy_list1.draw(screen)
            if self.score > 2:
                self.boss_list1.draw(screen)
            # Ifall alla fiender dör, börja skapa bossen, typ if len(enemy_hit_list) == antal fiender

        if self.level == 2:
            self.enemy_list1.draw(screen)
            self.enemy_list2.draw(screen)
            if self.score > 3:
                self.boss_list2.draw(screen)

        self.projectile_list.draw(screen)

        if not self.game_over:
            self.player_list.draw(screen)
            # fixa så den ritar fienderna efter du dött

        pygame.display.flip()