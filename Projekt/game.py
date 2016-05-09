import pygame
import random
import sprites
import graphics
import math
import Intro

ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY, SCREEN_HEIGHT, SCREEN_WIDTH = graphics.färger()

# Latemanslösning, se grafik

class Game(object):

    def __init__(self):

        # Attributes
        self.player_hp = 2
        self.level = 0 # Lägg till lvl -1 som är introskärm, lvl 0 som är meny??
        self.score = 0
        self.immortality = False
        self.highscore = 0
        self.highscore_message = False
        self.game_over = False
        self.current_time = 0
        self.time_death = 0
        self.cap = False

        ## Grafik
        #self.stars = graphics.Stars()

        # Astereoider
        # HP markörer

        # när du fixat snön på riktigt.

        # Create sprites lists, subklasser
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.boss_list1 = pygame.sprite.Group()
        self.boss_list2 = pygame.sprite.Group()
        self.enemy_list1 = pygame.sprite.Group()
        self.enemy_list2 = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        # två olika objekt i en spritegrupp och ifall de använder rätt update
        # göra en spritegroup i en spritegroup?
        # inte skapa allting i init, all_sprites innehåller bara det som används nu, och finns bara en lista

        # Player
        self.player = sprites.Player()
        self.player.image = pygame.Surface([30, 30])
        self.player.image.fill(WHITE)
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = SCREEN_WIDTH/2 - 15
        self.player.rect.y = 300
        self.player.move_x = 7
        self.player.move_y = 8
        self.player.original_posx = SCREEN_WIDTH/2 - 15
        self.player.original_posy = 300
        self.player_list.add(self.player)
        self.all_sprites_list.add(self.player)

        # Create the sprites

        # Level 1:

        for  i in range(21): # 20 st
            self.mobs1 = sprites.Enemies()
            if (i+1) < 11:
                self.mobs1.rect.x = SCREEN_WIDTH
                self.mobs1.move_x = -4
                self.mobs1.move_y = 4
                self.mobs1.rect.y = 0 + (-30 * i)
            if (i+1) >= 11:
                self.mobs1.rect.x = 0
                self.mobs1.move_x = 4
                self.mobs1.move_y = 4
                self.mobs1.rect.y = 300 + (-30 * i)
            self.mobs1.original_posx = self.mobs1.rect.x
            self.mobs1.original_posy = self.mobs1.rect.y
            # self.mobs1.choose_target(self.player.rect.x, self.player.rect.y)
            self.enemy_list.add(self.mobs1)
            self.enemy_list1.add(self.mobs1)
            self.all_sprites_list.add(self.mobs1)
            i += 1

        # testis
        #self.mobs1 = sprites.Enemies() # ta bort när du lägger till 20 st vanliga
        self.mobs1.rect.x = SCREEN_WIDTH / 2
        self.mobs1.rect.y = -50
        self.enemy_list.add(self.mobs1)
        self.enemy_list1.add(self.mobs1)
        self.all_sprites_list.add(self.mobs1)


        self.boss1 = sprites.Boss()
        self.boss1.rect.x = SCREEN_WIDTH / 2 - self.boss1.image.get_width()
        self.boss1.rect.y = -500
        self.boss1.active = 0
        #boss1.rect.y = 200 + 100*math.sin(math.radians(boss.rect.x))

        self.boss_list.add(self.boss1)
        self.boss_list1.add(self.boss1)
        self.all_sprites_list.add(self.boss1)


        # Level 2:
        for x in range(21):
            mobs2 = sprites.Enemies()
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

        for x in range(21):
            mobs2 = sprites.Enemies()
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

        self.boss2 = sprites.Boss()
        self.boss2.image = pygame.Surface([500,500])
        self.boss2.rect = self.boss2.image.get_rect()
        self.boss2.rect.x = SCREEN_WIDTH // 2 - self.boss2.image.get_width()
        self.boss2.rect.y = -1000
        self.boss2.active = 0
        self.boss_list.add(self.boss2)
        self.boss_list2.add(self.boss2)
        self.all_sprites_list.add(self.boss2)

    @property # Vad gör detta?
    def process_events(self): #(self, passed_time)

        self.session_time = pygame.time.get_ticks() #- passed_time

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        # passed_time = self.current_time # måste spara det utanför game för att det ska fungera
                        self.__init__()

                # För att testa lättare
                if event.key == pygame.K_q:
                    self.game_over = True
                if event.key == pygame.K_1:
                    self.level += 1
                if event.key == pygame.K_2:
                    self.level -= 1

                if not self.game_over:

                    self.player.movement(event, True)

                    if event.key == pygame.K_z:
                        #if len(self.projectile_list) < 10:
                        """
                        for x in range(2):
                            self.player_projectile = sprites.Projectile()
                            self.player_projectile.rect.x = self.player.rect.x + self.player.image.get_width() // 2\
                                                            - self.player_projectile.image.get_width() // 2 + -1^(x)\
                                                            * self.player.image.get_width() // (x+1)
                            #x * self.player.image.get_width() + -1^(x+1)*self.player_projectile.image.get_width()
                            self.player_projectile.rect.y = self.player.rect.y
                            self.all_sprites_list.add(self.player_projectile)
                            self.projectile_list.add(self.player_projectile)
                        """
                        for i in range(self.player.shots): # Fixa flera skott
                            self.player_projectile = sprites.Projectile()
                            self.player.shoot(1, self.player_projectile, self.all_sprites_list, self.projectile_list, 0, 0)

                    if event.key == pygame.K_x:

                        self.enemy_projectile = sprites.Enemyprojectile()
                        self.mobs1.shoot(1, self.enemy_projectile, self.all_sprites_list, self.projectile_list, 0, 0)

                    if event.key == pygame.K_y:

                        self.boss_projectile = sprites.Bossprojectile()
                        self.boss1.shoot(1, self.boss_projectile, self.all_sprites_list, self.projectile_list, self.player.rect.x, self.player.rect.y)


                        # bomb

            if event.type == pygame.KEYUP:

                self.player.movement(event, False)

    def run_logic(self):

            if self.player_hp < 1:
                self.game_over = True

            if self.session_time - self.time_death> 1500:
                self.immortality = False
                self.player.image.fill(WHITE)

            if not self.game_over:
                self.player.update()
                self.projectile_list.update()

                # Fungerar inte med flera sprites. Du måste få in player.pos i fiendeklassen.
                self.mobs1.choose_target(self.player.rect.x, self.player.rect.y) # effektivisera

                if self.immortality:
                    enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)
                else:
                    enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)

                boss_hit_list = pygame.sprite.spritecollide(self.player, self.boss_list, False)

                #### Groupcollide is a bit weird, doesnt really work here.
                #  groupcollide(group1, group2, dokill1, dokill2) -> dictionary
#
                #self.projectile_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.enemy_list, True, True)
                #self.projectile_boss_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.boss_list, True, False)
#
                #for self.player_projectile in self.projectile_list:
#
                #    for enemy in self.projectile_hit_list:
                #        self.score += 1
                #        print(self.score)
#
                #    for boss in self.projectile_boss_hit_list:
#
                #        if self.level == 1:
                #            self.boss1.hp -= self.player_projectile.damage
                #            print(self.boss1.hp)
#
                #        if self.level == 2:
                #            self.boss2.hp -= self.player_projectile.damage
                #            print(self.boss2.hp)
#
                #    if self.player_projectile.rect.y <= 0 or self.player_projectile.rect.y > SCREEN_HEIGHT:
                #        self.projectile_list.remove(self.player_projectile)
                #        self.all_sprites_list.remove(self.player_projectile)

#############################################################################################

                for self.player_projectile in self.projectile_list:
                    self.projectile_hit_list = pygame.sprite.spritecollide(self.player_projectile, self.enemy_list, True)
                    self.projectile_boss_hit_list = pygame.sprite.spritecollide(self.player_projectile, self.boss_list, False)

                    for enemy in self.projectile_hit_list:
                        self.projectile_list.remove(self.player_projectile)
                        self.all_sprites_list.remove(self.player_projectile)
                        self.score += 1
                        print(self.score)

                    for boss in self.projectile_boss_hit_list:
                        self.projectile_list.remove(self.player_projectile)
                        self.all_sprites_list.remove(self.player_projectile)

                        if self.level == 1:
                            self.boss1.hp -= self.player_projectile.damage
                            print(self.boss1.hp)

                        if self.level == 2:
                            self.boss2.hp -= self.player_projectile.damage
                            print(self.boss2.hp)

                    if self.player_projectile.rect.y <= 0 or self.player_projectile.rect.y > SCREEN_HEIGHT:
                        self.projectile_list.remove(self.player_projectile)
                        self.all_sprites_list.remove(self.player_projectile)

                ### samma for loop fast för bossskott.

                if not self.immortality:
                    for collision in enemy_hit_list:
                        self.score += 1
                        self.player_hp -= 1
                        self.player.reset_pos()
                        self.time_death = pygame.time.get_ticks()
                        self.immortality = True
                        self.player.image.fill(GREY)

                for collision in boss_hit_list:
                    self.game_over = True

                if self.score > self.highscore:
                    self.highscore = self.score

            # Level 0
            # if self.level == 0:

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

    def display_frame(self, screen):

        if self.level == -1: # Intro
            screen.fill(BLACK)

        if self.level == 0: # Meny
            screen.fill(NIGHTBLUE)
            graphics.stars(screen)


        if self.level == 1:
            screen.fill(NIGHTBLUE)

            graphics.stars(screen)

            #self.stars.draw_star(screen) # <- Av någon anledning funkar ej.
            # AttributeError: 'Stjärnor' object has no attribute 'snow_list'

            self.enemy_list1.draw(screen)
            if len(self.enemy_list1) == 0:
                self.boss_list1.draw(screen)
            # Grafik.draw_snow(screen)
#
        if self.level == 2:
            screen.fill(RED)
            graphics.stars(screen)
            # self.enemy_list1.draw(screen)
            self.enemy_list2.draw(screen)
            if len(self.enemy_list2) == 0:
                self.boss_list2.draw(screen)
#
        if self.level == 3:
            screen.fill(GREEN)

        # Overlay
        if self.level > 0:
            graphics.text(screen, 50, WHITE, str(self.score), 0, -300)
            graphics.text(screen, 50, WHITE, "HP", 550, -300)
            graphics.text(screen, 50, YELLOW, str(self.player_hp), 600, -300)
            graphics.text(screen, 50, WHITE, "Level", -600, -300)
            graphics.text(screen, 50, YELLOW, str(self.level), -500, -300)
            graphics.text(screen, 50, YELLOW, str(round(self.session_time / 1000, 1)) , -500, 300)
            graphics.text(screen, 50, WHITE, "Time", -600, 300)

        if not self.game_over:
            self.player_list.draw(screen)
            self.projectile_list.draw(screen)

        if self.game_over:

            graphics.text(screen, 150, WHITE, "Game Over", 0, 0)
            if self.highscore_message:
                graphics.text(screen, 150, STARBLUE, "NEW HIGH SCORE", 0, 200)

        pygame.display.flip()
