__author__ = 'Mr.Orange'

class meny_mark�r():
        def __init__(self):
            self.mark�r_y = 400

        def rita(self, mark�r_y):
            pygame.draw.rect(screen, WHITE, [150, mark�r_y, 30, 30])

        def r�relse(self, mark�r_y):
            if event.key == pygame.K_DOWN:
                    mark�r_y += 100
            elif event.key == pygame.K_UP:
                    mark�r_y -= 100
            return mark�r_y
