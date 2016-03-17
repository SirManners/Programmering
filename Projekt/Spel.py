import pygame
import random
import Klasser
import math
import Intro

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
        self.immortality = False
        self.level = 1
        # Lägg till lvl -1 som är introskärm, lvl 0 som är meny??
        self.score = 0
        self.highscore = 0
        self.highscore_message = False
        self.game_over = False
        self.time_1 = 0
        self.time_2 = 0

        self.ripmeddelande = Klasser.Text()
        self.ripmeddelande.font = 60
        self.ripmeddelande.title = "GAME OVER"

        # Grafik
        self.stjärnor = Klasser.Stjärnor()

        # Astereoider
        # HP markörer
        # stjärnor = Grafik
        # stjärnor.snö()
        # när du fixat snön på riktigt. Ha planeter i bakrunden annars?

        # Create sprites lists
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
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
        #self.bossprojektil = Bossprojektil()
        #self.all_sprites_list
        # Create the sprites

        # Level 1:
        i = 1
        for  x in range(20): # 20 st
            self.mobs1 = Klasser.Fiendermall()
            if i < 11:
                self.mobs1.rect.x = SCREEN_WIDTH
                self.mobs1.move_x = -4
                self.mobs1.move_y = 4
                self.mobs1.rect.y = 0 + (-30 * i)
            if i >= 11:
                self.mobs1.rect.x = 0
                self.mobs1.move_x = 4
                self.mobs1.move_y = 4
                self.mobs1.rect.y = 300 + (-30 * i)
            self.mobs1.original_posx = self.mobs1.rect.x
            self.mobs1.original_posy = self.mobs1.rect.y
            self.enemy_list.add(self.mobs1)
            self.enemy_list1.add(self.mobs1)
            self.all_sprites_list.add(self.mobs1)
            i += 1
        self.mobs1.choose_target(self.player.rect.x, self.player.rect.y)

        self.boss1 = Klasser.Bossmall()
        self.boss1.rect.x = SCREEN_WIDTH / 2 - self.boss1.image.get_width()
        self.boss1.rect.y = -500
        self.boss1.active = 0

        # ha den i update funk för att gå i kurva
        #boss1.rect.y = 200 + 100*math.sin(math.radians(boss.rect.x))

        self.boss_list.add(self.boss1)
        self.boss_list1.add(self.boss1)
        self.all_sprites_list.add(self.boss1)


        # Level 2:

        i = 0
        for x in range(20):
            mobs2 = Klasser.Fiendermall()
            mobs2.rect.y = 0 - x * 30
            mobs2.rect.x = 30
            mobs2.move_y = 3
            mobs2.move_x = 0
            mobs2.level = 2
            mobs2.grupp = 1
            mobs2.original_posx = mobs2.rect.x
            mobs2.original_posy = mobs2.rect.y
            self.enemy_list.add(mobs2)
            self.enemy_list2.add(mobs2)
            self.all_sprites_list.add(mobs2)

        for x in range(20):
            mobs2 = Klasser.Fiendermall()
            mobs2.rect.x = SCREEN_WIDTH - 50
            mobs2.rect.y = 0 - x * 30
            mobs2.move_y = 3
            mobs2.move_x = 0
            mobs2.level = 2
            mobs2.grupp = 2
            mobs2.original_posx = mobs2.rect.x
            mobs2.original_posy = mobs2.rect.y
            self.enemy_list.add(mobs2)
            self.enemy_list2.add(mobs2)
            self.all_sprites_list.add(mobs2)

        self.boss2 = Klasser.Bossmall()
        self.boss2.image = pygame.Surface([500,500])
        self.boss2.rect = self.boss2.image.get_rect()
        self.boss2.rect.x = SCREEN_WIDTH // 2 - self.boss2.image.get_width()
        self.boss2.rect.y = -1000
        self.boss2.active = 0
        self.boss_list.add(self.boss2)
        self.boss_list2.add(self.boss2)
        self.all_sprites_list.add(self.boss2)

    def process_events(self):

        self.time_1 = pygame.time.get_ticks()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.__init__()
                        self.score = 0

                if event.key == pygame.K_q:
                    self.game_over = True
                if event.key == pygame.K_1:
                    self.level += 1
                if event.key == pygame.K_2:
                    self.level -= 1

                if not self.game_over:

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player.player_up = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.player_down = True
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.player_left = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player.player_right = True

                    if event.key == pygame.K_z:
                        if len(self.projectile_list) < 2:
                            for x in range(2):
                                self.player_projektil = Klasser.Projektil() # Latemanslösning
                                self.player_projektil.rect = self.player_projektil.image.get_rect()
                                self.player_projektil.rect.x = self.player.rect.x + x * self.player.image.get_width() + -1^(x+1)*self.player_projektil.image.get_width()     #+ 5 + x*20
                                self.player_projektil.rect.y = self.player.rect.y
                                self.all_sprites_list.add(self.player_projektil)
                                self.projectile_list.add(self.player_projektil)
                        print(len(self.projectile_list))
                        # Begränsa antalet skott ute samtidigt?

                        # if event.key == pygame.K_x:
                        # bomb
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.player_up = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.player_down = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.player_left = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.player_right = False
                if event.key == pygame.K_x:
                    self.player.player_shoot = False

    def run_logic(self):

            #if not self.game_over:
            #    print("Nivå:", self.level)
            #    print("Score:", self.score)
            #    print("Hitpoints", self.player_hp)
            #print("Highscore", self.highscore)
            #print("--------------------------")
            #print(len(self.enemy_list1))
            #print(len(self.enemy_list2))

            # print(self.player_hp)

            # print(self.immortality)

            if self.player_hp < 1:
                self.game_over = True

            if self.time_1 - self.time_2 > 1500:
                self.immortality = False
                self.player.image.fill(WHITE)

            if not self.game_over:
                self.player.update()
                self.projectile_list.update()

                if self.immortality:
                    enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)
                else:
                    enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)

                boss_hit_list = pygame.sprite.spritecollide(self.player, self.boss_list, False)

                for self.player_projektil in self.projectile_list:
                    self.projectile_hit_list = pygame.sprite.spritecollide(self.player_projektil, self.enemy_list, True)
                    self.projectile_boss_hit_list = pygame.sprite.spritecollide(self.player_projektil, self.boss_list, False)

                    for enemy in self.projectile_hit_list:
                        self.projectile_list.remove(self.player_projektil)
                        self.all_sprites_list.remove(self.player_projektil)
                        self.score += 1

                    for boss in self.projectile_boss_hit_list:
                        # Lägg till boss HP som går ner när den träffas
                        self.projectile_list.remove(self.player_projektil)
                        self.all_sprites_list.remove(self.player_projektil)

                        if self.level == 1:
                            self.boss1.hp -= self.player_projektil.damage
                            print(self.boss1.hp)

                        if self.level == 2:
                            self.boss2.hp -= self.player_projektil.damage
                            print(self.boss2.hp)

                    if self.player_projektil.rect.y <= 0:
                        print("DELETED")
                        self.projectile_list.remove(self.player_projektil)
                        self.all_sprites_list.remove(self.player_projektil)

# Lägg till odödlighet efter att du krockat med en fiende och tappat liv

                if not self.immortality:
                    for collision in enemy_hit_list:
                        self.score += 1
                        self.player_hp -= 1
                        self.player.reset_pos()
                        self.time_2 = pygame.time.get_ticks()
                        self.immortality = True
                        self.player.image.fill(GREY)

                for collision in boss_hit_list:
                    self.game_over = True

            if self.game_over:
                if self.score > self.highscore:
                    self.highscore = self.score
                    self.highscore_message = True
                self.score = 0

            # Level 0
            # if self.level == 0:

            # Level 1
            if self.level == 1:
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

    def display_frame(self, screen):

        #if self.level == 0: # Fixa senare... du måste omstrukturera menyn också och allt.
        #    screen.fill(NIGHTBLUE)
        #    snow(screen)
        #    Intro.öppna_intro(screen)

        if self.level == 1:
            screen.fill(NIGHTBLUE)

            snow(screen)

            # self.stjärnor.draw_snow(screen) <- Av någon anledning funkar ej.
            # AttributeError: 'Stjärnor' object has no attribute 'snow_list'


            self.enemy_list1.draw(screen)
            if self.score > 2:
                self.boss_list1.draw(screen)
            # Grafik.draw_snow(screen)
#
        if self.level == 2:
            screen.fill(RED)
            snow(screen)
            # self.enemy_list1.draw(screen)
            self.enemy_list2.draw(screen)
            if self.score > 3:
                self.boss_list2.draw(screen)
#
        if self.level == 3:
            screen.fill(GREEN)

        if not self.game_over:
            self.player_list.draw(screen)
            self.projectile_list.draw(screen)

        if self.game_over:
            font = pygame.font.SysFont("system bold", 150)
            text = font.render("Game Over", True, WHITE)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            if self.highscore_message:
                font = pygame.font.SysFont("system bold", 150)
                text = font.render("NEW HIGHSCORE", True, STARBLUE)
                center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
                center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2) - 250
                screen.blit(text, [center_x, center_y])


        pygame.display.flip()
