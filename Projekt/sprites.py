import pygame
import random
import main
import math
import trig
import graphics

ROSA, BLACK, \
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

class Sprite_Mall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.move_x = 0
        self.move_y = 4
        self.level = 0
        self.hp = 1
        self.original_posx = 0
        self.original_posy = 0
        self.shots = 1

    def reset_pos(self):
        self.rect.x = self.original_posx
        self.rect.y = self.original_posy

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        if self.rect.y > SCREEN_HEIGHT + self.image.get_height():
            self.reset_pos()

    def shoot(self, amount, name, list1, list2, target_x, target_y):
        for x in range(amount): # i'm not really using this but it's a bother to remove
            self.image.get_rect()
            name.rect.x = self.rect.x + self.image.get_width() / 2 - name.image.get_width() / 2

            # Chooses which side of the sprite the bullets come from depending on movement
            if name.move_y < 0:
                name.rect.y = self.rect.y
            else:
                name.rect.y = self.rect.y + self.image.get_height()

            if name.track:
                name.target_x = target_x
                name.target_y = target_y

            list1.add(name)
            list2.add(name)

class Player(Sprite_Mall):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2 - 15
        self.rect.y = 300
        self.move_x = 7
        self.move_y = 8
        self.original_posx = SCREEN_WIDTH/2 - 15
        self.original_posy = 300

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        # Player movement and limitations so you cant leave the screen
        if self.up and self.rect.y > 0:
            self.rect.y -= self.move_y
        if self.down and self.rect.y < SCREEN_HEIGHT - self.image.get_height():
            self.rect.y += self.move_y
        if self.left and self.rect.x > 0:
            self.rect.x -= self.move_x
        if self.right and self.rect.x < SCREEN_WIDTH - self.image.get_width():
            self.rect.x += self.move_x

    def movement(self, event, boolean):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.up = boolean
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.down = boolean
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.left = boolean
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.right = boolean

class Enemies(Sprite_Mall):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.grupp = 0
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(-900, 0)
        self.target_x = -1
        self.target_y = -1
        self.move_x = 0
        self.move_y = 2
        self.infinite = True

    def choose_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

    def update(self):
        if self.rect.y > SCREEN_HEIGHT + 20:
            if self.infinite:
                self.kill()
            else:
                self.reset_pos()

        # Normal movement
        if self.target_x == -1 and self.target_y == -1:

            self.rect.x += self.move_x
            self.rect.y += self.move_y

            # For classic mode, preprogrammed moving pattern
            if self.level == 2:
                if self.rect.y > (SCREEN_HEIGHT // 5):
                    if self.grupp == 1:
                        self.move_x = 3
                    if self.grupp == 2:
                        self.move_x = -3

        # Track movement
        else:
            self.x_track_move, self.y_track_move = trig.vector_movement(
                self.rect.x,
                self.rect.y,
                self.target_x,
                self.target_y,
                self.move_y,
            )
            self.rect.x -= self.x_track_move
            self.rect.y -= self.y_track_move

class Boss(Enemies):
    def __init__(self):
        super().__init__()
        self.hp = 10
        self.total_hp = 10
        self.image = pygame.Surface([200, 200])
        self.rect = self.image.get_rect()
        self.image.fill(BLACK)
        self.projectile_number = 0
        self.rect.x = SCREEN_WIDTH / 2 - self.image.get_width()
        self.rect.y = -500
        self.frenzy = False

    def update(self):
        self.rect.y += 1 + 2*math.sin(math.radians(self.rect.x))
        self.rect.x += 1 + 2*math.sin(math.radians(self.rect.y))
        if self.hp / self.total_hp <= 0.25:
            self.frenzy = True
            self.image.fill([94, 11, 11])

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 10])
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.move_y = -15
        self.damage = 1
        self.track = True

    def update(self):
        self.rect.y += self.move_y

class Bossprojectile(Projectile):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROSA)
        self.move_y = 10
        self.target_x = -1
        self.target_y = -1
        self.track = True

        # Projectile movement
        self.x_track = 0
        self.y_track = 15

    def update(self):
        # makes the sprite shift in colour
        self.image.fill([random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)])

        if self.track:
            self.x_track, self.y_track = trig.vector_movement(
            self.rect.x,
            self.rect.y,
            self.target_x,
            self.target_y,
            self.move_y,
        )
            self.track = False
        self.rect.x -= self.x_track
        self.rect.y -= self.y_track
