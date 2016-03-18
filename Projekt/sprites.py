import pygame
import random
import main
import math
import trig

def färger():
    # --- Globala konstanter ---
    global ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY
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


    global SCREEN_HEIGHT, SCREEN_WIDTH
    SCREEN_HEIGHT = 688
    SCREEN_WIDTH = 1366

# Fixa importerbara färger
# --- Klasser ---

ROSA      = ( 255,   0, 132)
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
SCREEN_HEIGHT = 688
SCREEN_WIDTH = 1366

# Gör om så att både spelare och fiender båda är barn till samma klass, Mall klassen?
class Mall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.move_x = 0
        self.move_y = 0
        self.level = 0
        self.hp = 0
        self.original_posx = 0
        self.original_posy = 0

    def reset_pos(self):
        self.rect.x = self.original_posx
        self.rect.y = self.original_posy

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        if self.rect.y > SCREEN_HEIGHT + self.image.get_height():
            self.reset_pos()


class Player(Mall):
    def __init__(self):
        super().__init__()

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        # self.shoot = False

    def update(self):
        # tills vidare
        if self.up:
            self.rect.y -= self.move_y
        if self.down:
            self.rect.y += self.move_y
        if self.left:
            self.rect.x -= self.move_x
        if self.right:
            self.rect.x += self.move_x
       # if self.shoot:

    #def shoot(self, projectile_list):

    def movement(self, event, boolean):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.up = boolean
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.down = boolean
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.left = boolean
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.right = boolean

class Enemies(Mall):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.grupp = 0
        self.hit = False
        self.target_x = -1
        self.target_y = -1

    #def choose_target(self, target_x, target_y):
    #    self.target_x = target_x
    #    self.target_y = target_y
    #    print(self.target_x, self.target_y)

    def update(self):
        if self.target_x == -1 and self.target_y == -1:
            self.rect.x += self.move_x
            self.rect.y += self.move_y
            if self.rect.y > SCREEN_HEIGHT + 20:
                self.reset_pos()

            if self.level == 2:
                if self.rect.y > (SCREEN_HEIGHT // 5):
                    if self.grupp == 1:
                        self.move_x = 3
                    if self.grupp == 2:
                        self.move_x = -3

        else:
            #self.choose_target(self.target_x, self.target_y)
            self.x_move, self.y_move = trig.vector_movement(
                self.rect.x,
                self.rect.y,
                self.target_x,
                self.target_y,
                self.move_y
            )
            self.rect.x -= self.x_move
            self.rect.y -= self.y_move
            if self.rect.y > (SCREEN_HEIGHT + 20):
                self.reset_pos()

class Boss(Enemies):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.image = pygame.Surface([200, 200])
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)

    def update(self):
        self.rect.y += 1 + 2*math.sin(math.radians(self.rect.x))
        self.rect.x += 1 + 2*math.sin(math.radians(self.rect.y))

    # Bossen ska också skjuta
    # HP bar?

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        # Lägg till spelare här????
        super().__init__()
        self.image = pygame.Surface([4, 7])
        self.image.fill(YELLOW)
        self.move_y = -15
        self.damage = 10

    def update(self):
        self.rect.y += self.move_y

# class Missile(Projektil):
    # Tänker mig att den ska använda trig mot sin position och vara helt målsökande. Hur ska den välja vem den
    # siktar emot?


class Bossprojectile(pygame.sprite.Sprite): # Sen ska denna ärva Missile - klassen.
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.move_y = 15
        self.damage = 1

    def choose_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

    def update(self):
        self.rect.x, self.rect.y = Vektorer.vector_movement(
            self.rect.x,
            self.rect.y,
            self.target_x,
            self.target_y,
            self.move_y
        )

# Asteroider
