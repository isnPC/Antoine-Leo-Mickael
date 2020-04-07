import pygame
from classes import Joueur
from pygame.locals import *
pygame.init()



joueur = Joueur()

pygame.display.set_caption("jeu")
fenetre = pygame.display.set_mode((720, 480))
fond = pygame.image.load("assets/images.png").convert()
perso = pygame.image.load("assets/Untitled1.png").convert_alpha()
position_perso = perso.get_rect()

pygame.key.set_repeat(400, 30)
fenetre.blit(perso,position_perso)
jeu = True
while jeu:
    fenetre.blit(fond, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                position_perso = position_perso.move(0, 3)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                position_perso = position_perso.move(0, -3)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                position_perso = position_perso.move(3, 0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                position_perso = position_perso.move(-3, 0)
