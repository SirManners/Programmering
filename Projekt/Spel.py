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

class Fiender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def reset_pos(self):

    def update(self):


class Game(object):

    def __init__(self):

        self.game_over = False

    def process_events(self):

    def run_logic(self):

    def display_frame(self, screen):

