import pygame
from pygame.time import set_timer
from Chauve_souris import Chauve_souris


pygame.init()
#----------[Création de la fenêtre]---------#

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1000, 720))

#----------[Variables]----------#

bg = pygame.image.load("fond.png")
running = True
vague = 1

bar2vie100 = pygame.image.load('Barre2vie100.png')
bar2vie75 = pygame.image.load('Barre2vie75.png')
bar2vie50 = pygame.image.load('Barre2vie50.png')
bar2vie25 = pygame.image.load('Barre2vie25.png')
bar2vie0 = pygame.image.load('Barre2vie0.png')

v1 = [Chauve_souris(5, 500), Chauve_souris(15, 500)]
set_timer(pygame.USEREVENT, 60)

#-----[Fonctions]-----#

def barre2vie(mob):
    """Affiche les pvs du mob au dessus de sa tête"""
    if mob.health == mob.max_health:
        ecran.blit(bar2vie100, (mob.rect.x, mob.rect.y - 20))

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
                barre2vie(monstre)
                monstre.mouvements()




