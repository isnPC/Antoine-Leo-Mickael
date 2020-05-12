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

v1 = [Chauve_souris(5, 500), Chauve_souris(15, 500), Chauve_souris(15, 500), Chauve_souris(15, 500)]
set_timer(pygame.USEREVENT, 60)

#-----[Fonctions]-----#

def barre2vie(mob):
    """Affiche les pvs du mob au dessus de sa tête"""
    if mob.health == mob.max_health:
        ecran.blit(bar2vie100, (mob.rect.x + 10, mob.rect.y - 20))
    elif mob.health == mob.max_health*0.75:
        ecran.blit(bar2vie75, (mob.rect.x + 10, mob.rect.y - 20))
    elif mob.health == mob.max_health*0.5:
        ecran.blit(bar2vie50, (mob.rect.x + 10, mob.rect.y - 20))
    elif mob.health == mob.max_health*0.25:
        ecran.blit(bar2vie25, (mob.rect.x + 10, mob.rect.y - 20))
    elif mob.health == mob.max_health*0:
        ecran.blit(bar2vie0, (mob.rect.x + 10, mob.rect.y - 20))

def mort_mob(mob):
    if mob.health == 0:
        v1.remove(mob)



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
            barre2vie(monstre)
            mort_mob(monstre)


    for event in pygame.event.get():
        #-----[Gestion de la fermeture du jeu]-----#
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeu fermé")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                monstre.health = monstre.health - 25

        #-----[Mouvements Vague 1]-----#
        if event.type == pygame.USEREVENT:
            for monstre in v1:
                monstre.mouvements()





