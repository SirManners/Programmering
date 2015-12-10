import pygame
import random
import Klasser.färger

Klasser.färger()

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
        self.move_x = 1
        self.move_y = 1
        # self.remove_width
        # self.remove_height
    def reset_pos(self):

    def update(self):
        self.rect.y += self.move_y
        self.rect.x += self.move_x
        if 0 + self.rect.height > self.rect.x > SCREEN_WIDH + self.rect.height:

        if 0 + self.rect.width > self.rect.y > SCREEN_HEIGHT + self.rect.height:

class Game(object):

    def __init__(self):

        self.game_over = False

    def process_events(self):

    def run_logic(self):

    def display_frame(self, screen):

