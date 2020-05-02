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
spawn = 0
vague = 1
v1 = [Chauve_souris(), Chauve_souris()]

#-----[Fond Ecran]-----#

ecran.blit(bg, (0, 0))

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

    #-----[Vague 1]-----#

    if vague == 1 and spawn == 0:
        global spawn
        spawn = 1
        for monstre in v1:
            ecran.blit(monstre.image, (5, 500))

    #-----[Mouvements Vague 1]-----#

    else:
        m1_p = v1[0].mouvements()
        m2_p = v1[1].mouvements()
        ecran.blit(bg, (0, 0))
        ecran.blit(v1[0].image, m1_p)
        ecran.blit(v1[1].image, m2_p)










