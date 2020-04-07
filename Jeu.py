import pygame
pygame.init()
from Chauve_souris import Chauve_souris


#Création de la fenêtre :

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1000, 800))


bg = pygame.image.load("fond.png")

#game = pygame.Game()
Chauve_souris = Chauve_souris()

running = True

#Boucle Infinie
Chauve_souris.rect.x = Chauve_souris.rect.x + 100
Chauve_souris.rect.y = Chauve_souris.rect.y + 300
while running:
    ecran.blit(bg, (0, 0))
    ecran.blit(Chauve_souris.image,(Chauve_souris.rect.x, Chauve_souris.rect.y))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("jeu fermé")
        #Mouvements Monstres

        Chauve_souris.mouvements()
        #if monstre.rect.