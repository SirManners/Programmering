__author__ = 'Mr.Orange'

class meny_markör():
        def __init__(self):
            self.markör_y = 400

        def rita(self, markör_y):
            pygame.draw.rect(screen, WHITE, [150, markör_y, 30, 30])

        def rörelse(self, markör_y):
            if event.key == pygame.K_DOWN:
                    markör_y += 100
            elif event.key == pygame.K_UP:
                    markör_y -= 100
            return markör_y
