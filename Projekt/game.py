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
        self.difficulty = 20
        self.level = 0
        self.score = 0
        self.highscore = 0
        self.time_death = 0
        self.enemy_spawn = 1

        self.trigger_immortality = False
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
                            self.current_mobs.shoot(1, self.enemy_projectile, self.all_sprites_list, self.projectile_list, 0, 0)

                        # testis
                        if event.key == pygame.K_y:
                            self.boss_projectile = sprites.Bossprojectile()
                            self.current_boss.shoot(1, self.boss_projectile, self.all_sprites_list, self.projectile_list, self.player.rect.x, self.player.rect.y)

                        ############### BOMB ###############

                if event.type == pygame.KEYUP:
                    self.player.movement(event, False)

#########################################################################################################

    def run_logic(self):

        print(len(self.all_sprites_list))

        if self.player_hp <= 0 :
            self.game_over = True

        if self.session_time - self.time_death> 1500:
            self.immortality = False
            self.player.image.fill(WHITE)

        if not self.game_over:
            self.player.update()
            self.projectile_list.update()


            ############### Enemies colliding with player ###############
            if self.immortality:
                enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)
                boss_projectile_hit_list = pygame.sprite.groupcollide(self.enemy_projectile_list, self.player_list, False, False)

            else:
                enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
                boss_projectile_hit_list = pygame.sprite.groupcollide(self.enemy_projectile_list, self.player_list, True, False)

            boss_hit_list = pygame.sprite.spritecollide(self.player, self.boss_list, False)


            ############### Damage dealt to the player ###############
            if not self.immortality:
                for collision in enemy_hit_list:
                    self.score += 1
                    self.player_hp -= 1
                    self.trigger_immortality = True

                for collision in boss_projectile_hit_list:
                        self.player_hp -= 1
                        self.trigger_immortality = True

            if self.trigger_immortality:
                self.time_death = pygame.time.get_ticks()
                self.player.reset_pos()
                self.player.image.fill(GREY)
                self.trigger_immortality = False
                self.immortality = True

            for collision in boss_hit_list:
                self.game_over = True

            if self.score > self.highscore:
                self.highscore = self.score

            ############### Boss bullet removal ###############
            # if boss.projectile.rect.y > SCREEN HEIGHT:
                # self.all_sprites_list.remove ....

            ############### Player projectile hit registration ###############
            for self.player_projectile in self.projectile_list:
                self.projectile_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.enemy_list, True, True)
                self.projectile_boss_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.boss_list, True, False)

                for enemy in self.projectile_hit_list:
                    self.score += 1

                for boss in self.projectile_boss_hit_list:
                    self.current_boss.hp -= self.player_projectile.damage

                if self.player_projectile.rect.y <= 0 or self.player_projectile.rect.y > SCREEN_HEIGHT:
                    self.projectile_list.remove(self.player_projectile)
                    self.all_sprites_list.remove(self.player_projectile)


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
                for  i in range(self.difficulty): # 20 st
                    self.current_mobs = sprites.Enemies()

                    if i < self.difficulty / 2:
                        self.current_mobs.rect.x = SCREEN_WIDTH
                        self.current_mobs.move_x = -4
                        self.current_mobs.move_y = 4
                        self.current_mobs.rect.y = 0 + (-30 * i)

                    if i >= self.difficulty / 2:
                        self.current_mobs.rect.x = 0
                        self.current_mobs.move_x = 4
                        self.current_mobs.move_y = 4
                        self.current_mobs.rect.y = 300 + (-30 * i)

                    self.current_mobs.original_posx = self.current_mobs.rect.x
                    self.current_mobs.original_posy = self.current_mobs.rect.y
                    # self.mobs1.choose_target(self.player.rect.x, self.player.rect.y)
                    self.enemy_list.add(self.current_mobs)
                    self.all_sprites_list.add(self.current_mobs)

                ### Create boss sprites
                self.current_boss = sprites.Boss()
                self.current_boss.rect.x = SCREEN_WIDTH / 2 - self.current_boss.image.get_width()
                self.current_boss.rect.y = -500
                self.current_boss.active = 0
                self.boss_list.add(self.current_boss)
                self.all_sprites_list.add(self.current_boss)

                self.enemy_spawn += 1

        ############### Level 2 ###############
        if self.level == 2:
            if self.enemy_spawn == 2:
                for x in range(21):
                    self.current_mobs = sprites.Enemies()
                    self.current_mobs.rect.y = 0 - x * 30
                    self.current_mobs.rect.x = 30
                    self.current_mobs.move_y = 3
                    self.current_mobs.move_x = 0
                    self.current_mobs.level = 2
                    self.current_mobs.grupp = 1
                    self.current_mobs.original_posx = self.current_mobs.rect.x
                    self.current_mobs.original_posy = self.current_mobs.rect.y
                    self.enemy_list.add(self.current_mobs)
                    self.all_sprites_list.add(self.current_mobs)

                for x in range(21):
                    self.current_mobs = sprites.Enemies()
                    self.current_mobs.rect.x = SCREEN_WIDTH - 50
                    self.current_mobs.rect.y = 0 - x * 30
                    self.current_mobs.move_y = 3
                    self.current_mobs.move_x = 0
                    self.current_mobs.level = 2
                    self.current_mobs.grupp = 2
                    self.current_mobs.original_posx = self.current_mobs.rect.x
                    self.current_mobs.original_posy = self.current_mobs.rect.y
                    self.enemy_list.add(self.current_mobs)
                    self.all_sprites_list.add(self.current_mobs)

                # Skapa den inte först när alla fiender dött
                self.current_boss = sprites.Boss()
                self.current_boss.image = pygame.Surface([500, 500])
                self.current_boss.rect = self.current_boss.image.get_rect()
                self.current_boss.rect.x = SCREEN_WIDTH // 2 - self.current_boss.image.get_width()
                self.current_boss.rect.y = -1000
                self.current_boss.active = 0
                self.boss_list.add(self.current_boss)
                self.all_sprites_list.add(self.current_boss)

                self.enemy_spawn += 1

            # Enemy movement:
            #for mob in self.enemy_list:
            #    mob.target_x = self.player.rect.x
            #    mob.target_y = self.player.rect.y


        if self.level >= 1:
            # self.enemy_list1.choose_target(self.player.rect.x, self.player.rect.y) <- lägg till ifall de ska söka
            self.enemy_list.update()
            self.enemy_projectile_list.update()

            ### Spawns boss when all enemies are dead
            if len(self.enemy_list) == 0:
                if self.current_boss.active == 0:
                    if self.current_boss.active == 0:
                        self.current_boss.active += 1
                self.boss_list.update()

                ### Proceeds to next level when boss dies
                if self.current_boss.hp < 1:
                    self.level += 1
                    self.boss_list.remove(self.current_boss)
                    self.all_sprites_list.remove(self.current_boss)

                ### Makes the boss shoot while it's alive
                else:
                    if self.current_boss.projectile_number < 50 and not self.cap: # use sinus instead?
                        self.current_boss.projectile_number += 1
                        self.boss_projectile = sprites.Bossprojectile()
                        self.current_boss.shoot(
                            1,
                            self.boss_projectile,
                            self.all_sprites_list,
                            self.enemy_projectile_list,
                            self.player.rect.x,
                            self.player.rect.y
                            )

                    else:
                        self.cap = True
                        if self.current_boss.projectile_number > 1:
                            self.current_boss.projectile_number -= 1
                        else:
                            self.cap = False


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

        if self.level == 2:
            screen.fill(RED)
            graphics.stars(screen)

        if self.level == 3:
            screen.fill(GREEN)

        if self.level >= 1:
            self.enemy_list.draw(screen)
            self.enemy_projectile_list.draw(screen)
            if len(self.enemy_list) == 0:
                self.boss_list.draw(screen)


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