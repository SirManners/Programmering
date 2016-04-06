import pygame
import random
import main
import math
import trig
import graphics

ROSA, BLACK, WHITE, GREEN, RED, BROWN, YELLOW, BLUE, NIGHTBLUE, STARBLUE, GREY, SCREEN_HEIGHT, SCREEN_WIDTH = graphics.färger()

# göra en till klass som är barn till grupp och ändra den så att jag kan ha choose target o sånt?

class Mall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.move_x = 4
        self.move_y = 4
        self.level = 0
        self.hp = 0
        self.original_posx = 0
        self.original_posy = 0
        self.shots = 2

    def reset_pos(self):
        self.rect.x = self.original_posx
        self.rect.y = self.original_posy

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        if self.rect.y > SCREEN_HEIGHT + self.image.get_height():
            self.reset_pos()

    def shoot(self, amount, name, list1, list2, target_x, target_y):
        for x in range(amount): # funkar ej då bara en instans skapas i Game klassen
            self.image.get_rect()
            name.rect.x = self.rect.x + self.image.get_width()// 2\
                        - name.image.get_width() // 2 + -1^(x)\
                        * self.image.get_width() // (x+1)
            if name.move_y < 0:
                name.rect.y = self.rect.y
            else:
                name.rect.y = self.rect.y + self.image.get_height()

            if name.track:
                name.target_x = target_x
                name.target_y = target_y

            list1.add(name)
            list2.add(name)

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

    def choose_target(self, target_x, target_y): # Egentligen onödig
        self.target_x = target_x
        self.target_y = target_y

    def update(self):
        if self.rect.y > SCREEN_HEIGHT + 20:
                self.reset_pos()

        if self.target_x == -1 and self.target_y == -1:
            self.rect.x += self.move_x
            self.rect.y += self.move_y

            if self.level == 2:
                if self.rect.y > (SCREEN_HEIGHT // 5):
                    if self.grupp == 1:
                        self.move_x = 3
                    if self.grupp == 2:
                        self.move_x = -3

        else:
            self.x_track_move, self.y_track_move = trig.vector_movement(
                self.rect.x,
                self.rect.y,
                self.target_x,
                self.target_y,
                self.move_y
            )
            self.rect.x -= self.x_track_move
            self.rect.y -= self.y_track_move

class Boss(Enemies):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.image = pygame.Surface([200, 200])
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.active = 0

    def update(self):
        self.rect.y += 1 + 2*math.sin(math.radians(self.rect.x))
        self.rect.x += 1 + 2*math.sin(math.radians(self.rect.y))

    # HP bar?

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        # Lägg till spelare här????
        super().__init__()
        self.image = pygame.Surface([200, 7])
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.move_y = -15
        self.damage = 10
        self.track = False

    def update(self):
        self.rect.y += self.move_y

class Enemyprojectile(Projectile):
    def __init__(self):
        super().__init__()
        self.image.fill(GREEN)
        self.move_y = 15


#class Missile(Projectile):
    # Tänker mig att den ska använda trig mot sin position och vara helt målsökande. Hur ska den välja vem den
    # siktar emot?

class Bossprojectile(Enemyprojectile): # Sen ska denna ärva Missile - klassen.
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.move_y = 15
        self.damage = 1
        self.target_x = -1
        self.target_y = -1
        self.track = True
        self.x_track = 0 # otydligt namn
        self.y_track = 15 # otydligt namn

    def update(self):
        # if (self.rect.x - self.target_x) > 1 or (self.rect.y - self.target_y) > 1:
        if self.track:
            self.x_track, self.y_track = trig.vector_movement(
            self.rect.x,
            self.rect.y,
            self.target_x,
            self.target_y,
            self.move_y
        )
            self.track = False
        self.rect.x -= self.x_track
        self.rect.y -= self.y_track



# Asteroider
