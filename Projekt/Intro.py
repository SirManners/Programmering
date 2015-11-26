

def öppna_intro(screen):
    import Projekt.Klasser
    import pygame

    class Ridå(Projekt.Klasser.Rektangel):
        def __init__(self):
            super().__init__()

        def rörelse(self):
            self.x += self.change_x
            if self.y >= -769:
                self.y += self.change_y

    NIGHTBLUE = (   0,   1,  64)
    WHITE     = ( 255, 255, 255)
    RED       = ( 255,   0,   0)
    STARBLUE  = ( 159, 161, 252)
    BLACK     = (   0,   0,   0)

    ridå = Ridå()
    ridå.x = 0
    ridå.y = -500
    ridå.bredd = 1366
    ridå.höjd = 1268
    ridå.change_y = 3
    ridå.färg = WHITE

    spelnamn = Projekt.Klasser.Text()
    spelnamn.text = "Imse Vimse spindel / RYMDSPEl"
    spelnamn.x = 200
    spelnamn.y = 300
    spelnamn.colour = BLACK
    spelnamn.font = 100

    done = False
    clock = pygame.time.Clock()
    parameter = 0
    while not done:
        for event in pygame.event.get():
            # Gör att programet stängs när man trycker på en knapp
            if event.type == pygame.KEYDOWN:
                done = True
            if event.type == pygame.QUIT:
                print("User has asked to quit.")
                done = True

        # Färgen som fyller hela fönstret
        screen.fill(NIGHTBLUE)

        spelnamn.skriv(screen)

        ridå.rita(screen)
        ridå.rörelse()


        # Printar allting på skärmen
        pygame.display.flip()
        # Hur många gånger per sekund som skärmen uppdateras
        clock.tick(60)
        """parameter += 1
        if parameter == 4:
            done = True
        else:
            continue"""

