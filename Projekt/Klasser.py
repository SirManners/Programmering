import pygame
import random
import main
import math
import Vektorer

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
SCREEN_HEIGHT = 688
SCREEN_WIDTH = 1366



class Spelare(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2 - 15
        self.rect.y = 300
        self.move_x = 7
        self.move_y = 8
        self.player_up = False
        self.player_down = False
        self.player_left = False
        self.player_right = False
        self.player_shoot = False

    def reset_pos(self):
        self.rect.x = SCREEN_WIDTH/2 - 15
        self.rect.y = 300


    def update(self):
        # tills vidare
        if self.player_up:
            self.rect.y -= self.move_y
        if self.player_down:
            self.rect.y += self.move_y
        if self.player_left:
            self.rect.x -= self.move_x
        if self.player_right:
            self.rect.x += self.move_x
       # if self.player_shoot:

class Fiendermall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 0
        self.hp = 10
        self.level = 0
        self.grupp = 0
        self.hit = False
        # self.remove_width
        # self.remove_height

    def reset_pos(self):
        self.rect.x = self.original_posx
        self.rect.y = self.original_posy

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        if self.rect.y > SCREEN_HEIGHT + 20:
            self.reset_pos()
        # if self.rect.x >= SCREEN_WIDTH - self.image.get_width() or self.rect.x <= 0 + self.image.get_width():
            # self.move_x *= -1
        if self.hp < 1:
            print("JAG ÄR DÖD")

        if self.level == 2:
            if self.rect.y > (SCREEN_HEIGHT // 5):
                if self.grupp == 1:
                    self.move_x = 3
                if self.grupp == 2:
                    self.move_x = -3

        # if self.rect.y >= SCREEN_HEIGHT - self.image.get_height() or self.rect.y <= 0 - self.image.get_height():
            # self.move_y *= -1
        # if 0 + self.rect.height > self.rect.x > SCREEN_WIDTH + self.rect.height:
        # ta bort
        # if 0 + self.rect.width > self.rect.y > SCREEN_HEIGHT + self.rect.height:
        # ta bort

class Bossmall(Fiendermall):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.image = pygame.Surface([200, 200])
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.move_x = 0
        self.move_y = 2

    def update(self):
        self.rect.y += 1 + 2*math.sin(math.radians(self.rect.x))
        #self.move_y
        self.rect.x += 1 + 2*math.sin(math.radians(self.rect.y))
    # Bossen ska också skjuta

class Projektil(pygame.sprite.Sprite):
    def __init__(self):
        # Lägg till spelare här????
        super().__init__()
        self.image = pygame.Surface([4, 7])
        self.image.fill(YELLOW)
        self.move_y = -15
        self.damage = 10

    def update(self):
        self.rect.y += self.move_y

class Bossprojektil(Projektil):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.move_y = 15
        self.damage = 1

    def choose_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_Y

    def update(self):
        self.rect.x, self.rect.y = Vektorer.vector_movement(self.rect.x, self.rect.y, )
"""
class Boss(pygame.sprite.Sprite, Fiendermall):
    def __init__(self):
        super().__init__()
        # pygame.sprite.Sprite.__init__()
        # Fiendermall.__init__()

    def död(self):
        Game.level += 1

        # HP bars? Mer komplicerade attacker?


class Grafik:
    def __init_(self):
        self.snow_list = []
        self.snow_x = 0
        self.snow_y = 0
        # fixa så att det inte bara är snö som är grafik

    def snö(self):
        for i in range(50):
            self.snow_x = random.randrange(0, 1366)
            self.snow_y = random.randrange(-768, 0)
            self.snow_list.append([self.snow_x, self.snow_y])

    def draw_snow(self, screen):
        for i in range(len(self.snow_list)):
            pygame.draw.circle(screen, WHITE, self.snow_list[i], 2)
            self.snow_list[i][1] += 1
            if self.snow_list[i][1] > 768:
                y = random.randrange(-50, -10)
                self.snow_list[i][1] = y
                x = random.randrange(0, 1366)
                self.snow_list[i][0] = x


class Stjärnor(Grafik):
    def __init__(self):
        super().__init__()

"""


class Text(): # TRASIG
    def __init__(self):
        self.font = 36
        self.text = pygame.font.Font(None, self.font)
        self.title = ""
        self.bold = True
        self.colour = WHITE
        # self.x = (SCREEN_WIDTH // 2) - (self.text.get_width() // 2)
        # self.y = (SCREEN_HEIGHT // 2) - (self.text.get_height() // 2)
        self.x = 0
        self.y = 0


    def skriv(self, screen):
        self.text.render(self.title, self.bold, self.colour)
        screen.blit(self.title, [self.x, self.y])
"""

"""
class Rektangel():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.bredd = 0
        self.höjd = 0
        self.färg = [255, 255, 255]

    def rörelse(self):
        self.x += self.change_x
        self.y += self.change_y

    def rita(self, screen):
        pygame.draw.rect(screen, self.färg, [self.x, self.y, self.bredd, self.höjd])

class Ridå(Rektangel):
        def __init__(self):
            super().__init__()

        def rörelse(self):
            self.x += self.change_x
            if self.y >= -769:
                self.y += self.change_y