import pygame
pygame.init()
from Chauve_souris import Chauve_souris
from random import randint



#----------[Création de la fenêtre]---------#

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1000, 800))

#----------[Variables]----------#

bg = pygame.image.load("fond.png")
running = True
vague = 1
v1 = [Chauve_souris(5, 300), Chauve_souris(5, 500)]

#----------[Boucle Infinie]----------#

while running:
    #-----[Fond Ecran]-----#

    ecran.blit(bg, (0, 0))
    #-----[Mouvements]-----#

    if vague == 1:
        for monstre in v1:
            monstre.mouvements()
            ecran.blit(monstre.image, monstre.rect)

    #-----[Gestion de la fermeture du jeu]-----#

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    #-----[Actualisation]-----#

    pygame.display.flip()
    pygame.time.delay(100)


pygame.quit()
print("jeu fermé")



