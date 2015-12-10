import pygame
import random
import Klasser.färger

Klasser.färger()
SCREEN_HEIGHT = 688
SCREEN_WIDTH = 1366

class Spelare(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(30, 30)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        # piltangenter

class Fiendermall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
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

# class Projektil(pygame.sprite.Sprite):

class Game(object):

    def __init__(self):

        # Attributes
        self.score = 0
        self.game_over = False

        # Create sprites lists
        self.enemy_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        self.projectile_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.projectile_list)

        self.player = Spelare()
        self.all_sprites_list.add(self.player)

        # Create the sprites
        # Projektiler, skapa ifall variabel?
        boss = Fiendermall()

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

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()
            projectile_hit_list = pygame.sprite.spritecollide(self.projectile, self.enemy_list, True)
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy.list, True)

            for hit in enemy_hit_list:
                self.game_over = True
            for enemy in projectile_hit_list:
                self.score += 1

    def display_frame(self, screen):
        screen.fill(NIGHTBLUE)

        if self.game_over:
            """ rip meddelande """

        if  not self.game_over:
            self.all.sprites.list.draw(screen)

        pygame.display.flip