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
v1 = [Chauve_souris(), Chauve_souris()]

#-----[Fond Ecran]-----#

ecran.blit(bg, (0, 0))

#-----[Vagues de monstres]-----#

if vague == 1:
    for monstre in v1:
        ecran.blit(monstre.image, (5, 500))
        print('a')

#----------[Boucle Infinie]----------#

while running:
    #-----[Actualisation]-----#

    pygame.display.flip()

    #-----[Gestion de la fermeture du jeu]-----#

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("jeu fermé")

    #-----[Mouvements]-----#

    Chauve_souris.mouvements






