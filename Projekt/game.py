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
        self.player_hp = 10
        self.difficulty = 2 # recommended between 5-30
        self.level = 0
        self.score = 0
        self.highscore = 0
        self.time_death = 0
        self.enemy_spawn = 1

        self.trigger_immortality = False
        self.immortality = False
        self.highscore_message = False
        self.boss_active = False
        self.game_over = False
        self.victory = False
        self.infinite = False

        ### Menu
        self.menu_highscore =  False
        self.menu_help = False
        self.game_mode_picker = False
        self.difficulty_picker = False

        ### Create sprites lists, subklasser
        self.all_sprites_list = pygame.sprite.Group()
        self.boss_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.projectile_list = pygame.sprite.Group()
        self.enemy_projectile_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        ### Player
        self.player = sprites.Player()
        self.player_list.add(self.player)
        self.all_sprites_list.add(self.player)

        #########################################################################################################

    @property
    def process_events(self):

        self.session_time = pygame.time.get_ticks()

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

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

                        if self.game_mode_picker:
                            if self.player.rect.y == 300:
                                self.infinite = False
                            if self.player.rect.y == 400:
                                self.infinite = True
                            self.level += 1

                        if self.player.rect.y == 300:
                            self.game_mode_picker = True

                        if not self.game_mode_picker and self.player.rect.y == 400:
                            return True

            elif self.level != -1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True

                    if event.key == pygame.K_SPACE:
                        if self.game_over:
                            self.__init__()
                            self.level = 0

                    if event.key == pygame.K_q:
                        self.game_over = True

                    if not self.game_over:
                        self.player.movement(event, True)

                        ### Player shooting
                        if event.key == pygame.K_z:
                            for i in range(self.player.shots):
                                self.player_projectile = sprites.Projectile()
                                #alt sprites.Bossprojectile(), and then it shoots towards mouse pos
                                self.player.shoot(
                                    1,
                                    self.player_projectile,
                                    self.all_sprites_list,
                                    self.projectile_list,
                                    self.mouse_x,
                                    self.mouse_y
                                    )

                if event.type == pygame.KEYUP:
                    self.player.movement(event, False)

                # if event.type == pygame.mouse. to make it shoot when clicking

#########################################################################################################

    def run_logic(self):

        if self.player_hp <= 0:
            self.player.kill()
            self.game_over = True

        # Makes the player blink before becoming mortal again
        if self.session_time - self.time_death> 500:
            if self.session_time % 2 == 0:
                self.player.image.fill(WHITE)
            else:
                self.player.image.fill(GREY)

        ### Reset immortality
        if self.session_time - self.time_death> 1000:
            self.immortality = False
            self.player.image.fill(WHITE)

        if not self.game_over:

            ############### Enemies colliding with player ###############
            if self.immortality:
                enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, False)
                enemy_projectile_hit_list = pygame.sprite.groupcollide(self.enemy_projectile_list, self.player_list, False, False)

            else:
                enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
                enemy_projectile_hit_list = pygame.sprite.groupcollide(self.enemy_projectile_list, self.player_list, True, False)

            boss_hit_list = pygame.sprite.spritecollide(self.player, self.boss_list, False)

            ############### Damage dealt to the player ###############
            if not self.immortality:
                for collision in enemy_hit_list:
                    self.score += 1
                    self.player_hp -= 1
                    self.trigger_immortality = True

                for collision in enemy_projectile_hit_list:
                        self.player_hp -= 1
                        self.trigger_immortality = True

            if self.trigger_immortality:
                self.time_death = pygame.time.get_ticks()
                #self.player.reset_pos()
                self.player.image.fill(GREY)
                self.trigger_immortality = False
                self.immortality = True

            for collision in boss_hit_list:
                self.player.kill()
                self.game_over = True

            ############### Player projectile hit registration ###############
            for self.player_projectile in self.projectile_list:
                self.projectile_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.enemy_list, True, True)
                self.projectile_boss_hit_list = pygame.sprite.groupcollide(self.projectile_list, self.boss_list, True, False)

                for enemy in self.projectile_hit_list:
                    self.score += 1

                for boss in self.projectile_boss_hit_list:
                    self.current_boss.hp -= self.player_projectile.damage

                if self.player_projectile.rect.y <= 0 or self.player_projectile.rect.y > SCREEN_HEIGHT:
                    self.player_projectile.kill()


        ############### Level -1, Intro ###############
        if self.level == -1:
            self.intro.update()
            if self.intro.y > 1500:
                self.level += 1

        ############## Infinite ##############
        if self.infinite:

            # Enemy movement:                           # for mobs tracking the player
            #for mob in self.enemy_list:
            #    mob.target_x = self.player.rect.x
            #    mob.target_y = self.player.rect.y

            if not self.boss_active and self.enemy_spawn % 2 == 1:
                for i in range(self.difficulty * (self.level + 1)):
                    self.current_mobs = sprites.Enemies()
                    self.current_mobs.move_y = 2 * self.level
                    self.current_mobs.rect.y = random.randrange(-900 * (0.5 * self.level), 0)
                    self.enemy_list.add(self.current_mobs)
                    self.all_sprites_list.add(self.current_mobs)

                self.enemy_spawn += 1


            if not self.boss_active and len(self.enemy_list) == 0:
                self.boss_active = True
                self.current_boss = sprites.Boss()
                self.current_boss.hp = self.difficulty * self.level
                self.current_boss.total_hp = self.current_boss.hp
                self.boss_list.add(self.current_boss)
                self.all_sprites_list.add(self.current_boss)

                self.enemy_spawn -= 1


        ############## Classic ############## (more gritty code)
        if not self.infinite:

        ############### Level 1 ###############
            if self.level == 1:
                if self.enemy_spawn == 1:

                    ### Create enemy sprites
                    for  i in range(self.difficulty): # 20 st
                        self.current_mobs = sprites.Enemies()
                        self.current_mobs.infinite = False

                        if i < self.difficulty / 2:
                            self.current_mobs.rect.x = SCREEN_WIDTH
                            self.current_mobs.move_x = -2 # -4
                            self.current_mobs.move_y = 3 # 4
                            self.current_mobs.rect.y = 0 + (-30 * i)

                        if i >= self.difficulty / 2:
                            self.current_mobs.rect.x = 0
                            self.current_mobs.move_x = 2 # 4
                            self.current_mobs.move_y = 3 # 4
                            self.current_mobs.rect.y = 300 + (-30 * i)

                        self.current_mobs.original_posx = self.current_mobs.rect.x
                        self.current_mobs.original_posy = self.current_mobs.rect.y

                        self.enemy_list.add(self.current_mobs)
                        self.all_sprites_list.add(self.current_mobs)

                    self.enemy_spawn += 1

                ### Spawns boss when all enemies are dead
                if len(self.enemy_list) == 0:
                    if self.enemy_spawn == 2:
                        ### Create boss sprites
                        self.boss_active = True
                        self.current_boss = sprites.Boss()
                        self.current_boss.hp = self.difficulty * 2
                        self.current_boss.total_hp = self.current_boss.hp
                        self.boss_list.add(self.current_boss)
                        self.all_sprites_list.add(self.current_boss)

                        self.enemy_spawn += 1

            ############### Level 2 ############### Same but for lvl 2
            if self.level == 2:
                if self.enemy_spawn == 3:

                    for x in range(self.difficulty): # 21
                        self.current_mobs = sprites.Enemies()
                        self.current_mobs.rect.y = 0 - x * 30
                        self.current_mobs.rect.x = 30
                        self.current_mobs.move_y = 2 # 3
                        self.current_mobs.move_x = 0
                        self.current_mobs.level = 2
                        self.current_mobs.grupp = 1
                        self.current_mobs.infinite = False
                        self.current_mobs.original_posx = self.current_mobs.rect.x
                        self.current_mobs.original_posy = self.current_mobs.rect.y
                        self.enemy_list.add(self.current_mobs)
                        self.all_sprites_list.add(self.current_mobs)

                    for x in range(self.difficulty): # 21
                        self.current_mobs = sprites.Enemies()
                        self.current_mobs.rect.x = SCREEN_WIDTH - 50
                        self.current_mobs.rect.y = 0 - x * 30
                        self.current_mobs.move_y = 2 # 3
                        self.current_mobs.move_x = 0
                        self.current_mobs.level = 2
                        self.current_mobs.grupp = 2
                        self.current_mobs.infinite = False
                        self.current_mobs.original_posx = self.current_mobs.rect.x
                        self.current_mobs.original_posy = self.current_mobs.rect.y
                        self.enemy_list.add(self.current_mobs)
                        self.all_sprites_list.add(self.current_mobs)

                    self.enemy_spawn += 1

            ### Spawns boss when all enemies are dead
            if len(self.enemy_list) == 0:

                if self.enemy_spawn == 4:
                    self.boss_active = True
                    self.current_boss = sprites.Boss()
                    self.current_boss.hp = self.difficulty * 2
                    self.current_boss.total_hp = self.current_boss.hp
                    self.current_boss.image = pygame.Surface([500, 500])
                    self.current_boss.rect = self.current_boss.image.get_rect()
                    self.current_boss.rect.x = SCREEN_WIDTH // 2 - self.current_boss.image.get_width()
                    self.current_boss.rect.y = -1000
                    self.boss_list.add(self.current_boss)
                    self.all_sprites_list.add(self.current_boss)

                    self.enemy_spawn += 1

            if self.level == 3:
                self.game_over = True
                self.victory = True

        ### General logic
        if self.level >= 1:

            self.all_sprites_list.update()

            ### Makes the enemies shoot
            for mob in self.enemy_list:
                if self.session_time % random.randrange(1163, 1223) == 0:
                    self.enemy_projectile = sprites.Bossprojectile()
                    self.enemy_projectile.move_y = 3
                    self.enemy_projectile.image = pygame.Surface([10,10])
                    mob.shoot(
                        1,
                        self.enemy_projectile,
                        self.all_sprites_list,
                        self.enemy_projectile_list,
                        self.player.rect.x,
                        self.player.rect.y
                    )

            ### Proceeds to next level when boss dies
            if self.boss_active:
                if self.current_boss.hp < 1:
                    self.level += 1
                    self.boss_active = False
                    self.current_boss.kill()

            ### Makes the boss shoot while it's alive
                else:
                    if self.current_boss.frenzy:
                        frequency = 3
                    else:
                        frequency = 13

                    if self.session_time % frequency == 0:
                        self.boss_projectile = sprites.Bossprojectile()
                        self.current_boss.shoot(
                            3,
                            self.boss_projectile,
                            self.all_sprites_list,
                            self.enemy_projectile_list,
                            self.player.rect.x,
                            self.player.rect.y
                            )

            ############### Boss bullet removal ###############
            for projectile in self.enemy_projectile_list:
                if projectile.rect.y > SCREEN_HEIGHT:
                    projectile.kill()



#########################################################################################################

    def display_frame(self, screen):

        screen.fill(NIGHTBLUE)
        graphics.stars(screen)

        if self.level == -1: # Intro
            graphics.text(screen, 150, WHITE, str("SQUARESHOOTER"), -200, -200)
            self.intro.draw(screen)

        if self.level == 0: # Meny

            if self.game_mode_picker:
                graphics.text(screen, 70, WHITE, str("CLASSIC"), 200, -27)
                graphics.text(screen, 70, WHITE, str("INFINITE"), 200, 73)

            else:
                graphics.text(screen, 70, WHITE, str("PLAY"), 200, -27)
                graphics.text(screen, 70, WHITE, str("QUIT"), 200, 73)

        if self.level > 0 and self.level %2 == 0:
            screen.fill(RED)
            graphics.stars(screen)

        if self.level >= 1:
            self.all_sprites_list.draw(screen)

        # Overlay
        if self.level > 0:
            graphics.text(screen, 50, WHITE, str(self.score), 0, -300)
            graphics.text(screen, 50, WHITE, "HP", 550, -300)
            graphics.text(screen, 50, YELLOW, str(self.player_hp), 600, -300)
            graphics.text(screen, 50, WHITE, "Level", -600, -300)
            graphics.text(screen, 50, YELLOW, str(self.level), -500, -300)
            graphics.text(screen, 50, YELLOW, str(round(self.session_time / 1000, 1)) , -500, 300)
            graphics.text(screen, 50, WHITE, "Time", -600, 300)

            # Boss HP Bar
            if self.boss_active:
                graphics.rect(
                    screen,
                    0,
                    SCREEN_HEIGHT - 20,
                    SCREEN_WIDTH - (self.current_boss.total_hp - self.current_boss.hp) * (SCREEN_WIDTH / self.current_boss.total_hp),
                    20,
                    BLUE
                )

        # Draws player when in menue
        if not self.game_over:
            self.player_list.draw(screen)

        if self.game_over:
            if self.victory:
                graphics.text(screen, 150, WHITE, str("YOU ARE WINNER"), 0, 0)
                if self.highscore_message:
                    graphics.text(screen, 150, STARBLUE, "NEW HIGH SCORE", 0, 200)
            else:
                graphics.text(screen, 150, WHITE, "Game Over", 0, 0)
                if self.highscore_message:
                    graphics.text(screen, 150, STARBLUE, "NEW HIGH SCORE", 0, 200)

        pygame.display.flip()

#########################################################################################################