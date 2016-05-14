import pygame
import random
import sprites
import graphics
import math
import trig

ROSA, \
BLACK, \
WHITE, \
GREEN, \
RED, \
BROWN, \
YELLOW, \
BLUE, \
NIGHTBLUE, \
STARBLUE, \
GREY, \
SCREEN_HEIGHT, \
SCREEN_WIDTH = \
    graphics.colour()

class Game(object):

    def __init__(self):

        ### Attributes
        self.player_hp = 2
        self.difficulty = 4
        self.level = 0
        self.score = 0
        self.highscore = 0
        self.time_death = 0
        self.enemy_spawn = 1

        self.immortality = False
        self.cap = False
        self.highscore_message = False
        self.game_over = False

        ### Menu
        self.menu_highscore =  False
        self.menu_help = False

        ### Graphics
        self.intro = graphics.Rectangle() # lägg in cool bild här
        # More fancy intro
        #self.stars = graphics.Stars()
        # Astereoider
        # HP bar for boss <---------------------------------------------------------!!!!!!!!!!!!!!!!!!!!!!!


        ### Create sprites lists, subklasser
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.enemy_projectile_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        # två olika objekt i en spritegrupp och ifall de använder rätt update
        # göra en spritegroup i en spritegroup?
        # inte skapa allting i init, all_sprites innehåller bara det som används nu, och finns bara en lista

        ### Player
        self.player = sprites.Player()
        self.player_list.add(self.player)
        self.all_sprites_list.add(self.player)

        ### Enemies setup

        #########################################################################################################

    @property # Vad gör detta?
    def process_events(self): #(self, passed_time)

        self.session_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if self.level == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True

                    if event.key == pygame.K_UP:
                        if self.player.rect.y > 300:
                            self.player.rect.y -= 100

                    if event.key == pygame.K_DOWN:
                        if self.player.rect.y < 600:
                            self.player.rect.y += 100

                    if event.key == pygame.K_RETURN:
                        if self.player.rect.y == 300:
                            self.level += 1

                        if self.menu_help or self.menu_highscore:
                            self.menu_help = False
                            self.menu_highscore = False

                        if self.player.rect.y == 400:
                            self.menu_highscore == True
                            print(self.menu_highscore)

                        if self.player.rect.y == 600:
                            return True

            elif self.level != -1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True

                    if event.key == pygame.K_SPACE:
                        if self.game_over:
                            # passed_time = self.current_time # måste spara det utanför game för att det ska fungera
                            self.__init__()
                            self.level = 0

                    if event.key == pygame.K_q:
                        self.game_over = True

                    if event.key == pygame.K_1:
                        self.level += 1

                    if event.key == pygame.K_2:
                        self.level -= 1

                    if not self.game_over:
                        self.player.movement(event, True)

                        ### Player shooting
                        if event.key == pygame.K_z:
                            #if len(self.projectile_list) < 10: Limit the amount of shots?
                            for i in range(self.player.shots): # Fixa flera skott
                                self.player_projectile = sprites.Projectile()
                                self.player.shoot(1, self.player_projectile, self.all_sprites_list, self.projectile_list, 0, 0)

                        # testis
                        if event.key == pygame.K_x:
                            self.enemy_projectile = sprites.Enemyprojectile()
                            self.mobs1.shoot(1, self.enemy_projectile, self.all_sprites_list, self.projectile_list, 0, 0)

                        # testis
                        if event.key == pygame.K_y:
                            self.boss_projectile = sprites.Bossprojectile()
                            self.boss1.shoot(1, self.boss_projectile, self.all_sprites_list, self.projectile_list, self.player.rect.x, self.player.rect.y)

                        ############### BOMB ###############

                if event.type == pygame.KEYUP:
                    self.player.movement(event, False)

#########################################################################################################

    def run_logic(self):

        if self.player_hp <= 0 :
            self.game_over = True

        if self.session_time - self.time_death> 1500:
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

            ############### Player projectile hit registration ###############

            for self.player_projectile in self.projectile_list:
                self.projectile_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.enemy_list, True, True)
                self.projectile_boss_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.boss_list, True, False)
                #self.projectile_hit_list = pygame.sprite.spritecollide(self.player_projectile, self.enemy_list, True)
                #self.projectile_boss_hit_list = pygame.sprite.spritecollide(self.player_projectile, self.boss_list, False)

                print(len(self.projectile_list))

                for enemy in self.projectile_hit_list:
                    self.score += 1


                for boss in self.projectile_boss_hit_list:

                    if self.level == 1: # current_boss osv
                        self.boss1.hp -= self.player_projectile.damage
                        print(self.boss1.hp)

                    if self.level == 2:
                        self.boss2.hp -= self.player_projectile.damage
                        print(self.boss2.hp)

                if self.player_projectile.rect.y <= 0 or self.player_projectile.rect.y > SCREEN_HEIGHT:
                    self.projectile_list.remove(self.player_projectile)
                    self.all_sprites_list.remove(self.player_projectile)

            ############### Boss projectile hit registration ###############

            for self.boss_projectile in self.enemy_projectile_list:
                self.boss_projectile_hit_list = pygame.sprite.spritecollide(self.boss_projectile, self.player_list, False)

                for player in self.boss_projectile_hit_list:
                    if not self.immortality:
                        self.player_hp -= 0.05

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

        ############### Level -1, Intro ###############
        if self.level == -1:
            self.intro.update()
            if self.intro.y > 1500:
                self.level += 1

        ############### Level 1 ###############
        if self.level == 1:
            # create function that creates levels of sprites
            if self.enemy_spawn == 1:

                ### Create enemy sprites
                for  i in range(self.difficulty + 1): # 20 st
                    self.mobs1 = sprites.Enemies()

                    if i < self.difficulty / 2:
                        self.mobs1.rect.x = SCREEN_WIDTH
                        self.mobs1.move_x = -4
                        self.mobs1.move_y = 4
                        self.mobs1.rect.y = 0 + (-30 * i)

                    if i >= self.difficulty / 2:
                        self.mobs1.rect.x = 0
                        self.mobs1.move_x = 4
                        self.mobs1.move_y = 4
                        self.mobs1.rect.y = 300 + (-30 * i)

                    self.mobs1.original_posx = self.mobs1.rect.x
                    self.mobs1.original_posy = self.mobs1.rect.y
                    # self.mobs1.choose_target(self.player.rect.x, self.player.rect.y)
                    self.enemy_list.add(self.mobs1)
                    self.all_sprites_list.add(self.mobs1)
                    i += 1

                ### Testis, rörelsen fungerar inte med flera sprites.
                # Köra igenom sprite_listen med spritsen i för att få flera att göra det.
                self.mobs1.rect.x = SCREEN_WIDTH / 2
                self.mobs1.rect.y = -50
                self.enemy_list.add(self.mobs1)
                self.all_sprites_list.add(self.mobs1)

                ### Create boss sprites
                self.boss1 = sprites.Boss()
                self.boss1.rect.x = SCREEN_WIDTH / 2 - self.boss1.image.get_width()
                self.boss1.rect.y = -500
                self.boss1.active = 0
                self.boss_list.add(self.boss1)
                self.all_sprites_list.add(self.boss1)

                self.enemy_spawn += 1

            ### Spawns boss when all enemies are dead
            if len(self.enemy_list) == 0:
                if self.boss1.active == 0:
                    if self.boss1.active == 0:
                        self.boss1.active += 1
                self.boss_list.update()

                ### Proceeds to next level when boss dies
                if self.boss1.hp < 1:
                    self.level += 1
                    self.boss_list.remove(self.boss1)

                ### Makes the boss shoot while it's alive
                else:
                    if self.boss1.projectile_number < 50 and not self.cap: # use sinus instead?
                        self.boss1.projectile_number += 1
                        self.boss_projectile = sprites.Bossprojectile()
                        self.boss1.shoot(
                            1,
                            self.boss_projectile,
                            self.all_sprites_list,
                            self.projectile_list,
                            self.player.rect.x,
                            self.player.rect.y
                            )

                    else:
                        self.cap = True
                        if self.boss1.projectile_number > 1:
                            self.boss1.projectile_number -= 1
                        else:
                            self.cap = False

            else:
                # self.enemy_list1.choose_target(self.player.rect.x, self.player.rect.y) <- lägg till ifall de ska söka
                self.enemy_list.update()
                self.enemy_projectile_list.update()

        ############### Level 2 ###############
        if self.level == 2:
            if self.enemy_spawn == 2:
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
                    self.all_sprites_list.add(mobs2)

                # Skapa den inte först när alla fiender dött
                self.boss2 = sprites.Boss()
                self.boss2.image = pygame.Surface([500,500])
                self.boss2.rect = self.boss2.image.get_rect()
                self.boss2.rect.x = SCREEN_WIDTH // 2 - self.boss2.image.get_width()
                self.boss2.rect.y = -1000
                self.boss2.active = 0
                self.boss_list.add(self.boss2)
                self.all_sprites_list.add(self.boss2)

                self.enemy_spawn += 1

            # Enemy movement:
            for mob in self.enemy_list:
                mob.target_x = self.player.rect.x
                mob.target_y = self.player.rect.y

            if len(self.enemy_list) == 0:
                if self.boss2.active == 0:
                    print("Boss has spawned")
                    self.boss2.active += 1
                self.boss_list.update()

                if self.boss2.hp < 1:
                    self.level += 1
                    self.boss_list.remove(self.boss2)

            else:
                self.enemy_list.update()

#########################################################################################################

    def display_frame(self, screen):

        if self.level == -1: # Intro
            screen.fill(NIGHTBLUE)
            graphics.stars(screen)
            self.intro.draw(screen) # Piffa upp introt
            # Add the name of the game

        if self.level == 0: # Meny
            screen.fill(NIGHTBLUE)
            graphics.stars(screen)

            if not self.menu_highscore and not self.menu_help:
                graphics.text(screen, 70, WHITE, str("PLAY"), 200, -27)
                graphics.text(screen, 70, WHITE, str("HIGHSCORE"), 200, 73)
                graphics.text(screen, 70, WHITE, str("HELP"), 200, 173)
                graphics.text(screen, 70, WHITE, str("QUIT"), 200, 273)
            else:
                graphics.text(screen, 70, WHITE, str("BACK"), 200, self.player.rect.y)

        if self.level == 1:
            screen.fill(NIGHTBLUE)
            graphics.stars(screen)
            #self.stars.draw_star(screen) # <- Av någon anledning funkar ej.
            # AttributeError: 'Stjärnor' object has no attribute 'snow_list'

            self.enemy_list.draw(screen)
            if len(self.enemy_list) == 0:
                self.boss_list.draw(screen)

        if self.level == 2:
            screen.fill(RED)
            graphics.stars(screen)

            self.enemy_list.draw(screen)
            if len(self.enemy_list) == 0:
                self.boss_list.draw(screen)

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

#########################################################################################################