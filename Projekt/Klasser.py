import pygame
import random


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
        self.move_x = 4
        self.move_y = 6
        self.player_up = False
        self.player_down = False
        self.player_left = False
        self.player_right = False
        self.player_shoot = False

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
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.move_x = 0
        self.move_y = 2
        # self.remove_width
        # self.remove_height

    def reset_pos(self):
        self.rect.y = 0 - self.image.get_height()

    def update(self):

        self.rect.y += self.move_y
        if self.rect.y > SCREEN_HEIGHT + 70:
            self.reset_pos()
        # if self.rect.x >= SCREEN_WIDTH - self.image.get_width() or self.rect.x <= 0 + self.image.get_width():
            # self.move_x *= -1
        self.rect.x += self.move_x
        # if self.rect.y >= SCREEN_HEIGHT - self.image.get_height() or self.rect.y <= 0 - self.image.get_height():
            # self.move_y *= -1
        # if 0 + self.rect.height > self.rect.x > SCREEN_WIDTH + self.rect.height:
        # ta bort
        # if 0 + self.rect.width > self.rect.y > SCREEN_HEIGHT + self.rect.height:
        # ta bort

class Bossmall(Fiendermall):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([200, 200])
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.move_x = 0
        self.move_y = 4


class Projektil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(YELLOW)
        print("Jag finns")
        self.rect = self.image.get_rect()
        self.move_y = -3
        # Få ut spelarens x och y värde ur dess klass i main
        self.rect.y = 0
        self.rect.x = 0

    def update(self):
        self.rect.y += self.move_y
        print("Jag finns fortfarande")
        # någonting görs true i en lista med alla projektiler när du klickar på shoot,
        # sätts false när de lämnar skärmen eller krockar.

    # def reset_pos(self):
        # ta bort den på något sätt

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

