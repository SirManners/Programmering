import pygame


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

WHITE     = ( 255, 255, 255)
SCREEN_HEIGHT = 688
SCREEN_WIDTH = 1366


class Text():
    def __init__(self):
        self.text = ""
        self.bold = True
        self.colour = WHITE
        # ändrat till screen width osv
        # self.x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
        # self.y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
        self.x = 0
        self.y = 0
        self.font = 36

    def skriv(self, screen):
        text = pygame.font.Font(None, self.font).render(self.text, self.bold, self.colour)
        screen.blit(text, [self.x, self.y])


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

