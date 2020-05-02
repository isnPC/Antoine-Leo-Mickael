import pygame
from pygame.time import set_timer
from Chauve_souris import Chauve_souris


pygame.init()
#----------[Création de la fenêtre]---------#

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1000, 800))

#----------[Variables]----------#

bg = pygame.image.load("fond.png")
running = True
vague = 1

v1 = [Chauve_souris(5, 500), Chauve_souris(15, 500)]
set_timer(pygame.USEREVENT, 10)

#-----[Fond Ecran]-----#

ecran.blit(bg, (0, 0))

#----------[Boucle Infinie]----------#

while running:

    #-----[Actualisation]-----#

    pygame.display.flip()

    ecran.blit(bg, (0, 0))

    #-----[Vague 1]-----#

    if vague == 1:
        for monstre in v1:
            ecran.blit(monstre.image, monstre.rect)

    for event in pygame.event.get():
        #-----[Gestion de la fermeture du jeu]-----#
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeu fermé")

        #-----[Mouvements Vague 1]-----#
        if event.type == pygame.USEREVENT:
            for monstre in v1:
                monstre.mouvements()










