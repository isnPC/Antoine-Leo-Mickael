import pygame
pygame.init()
from monstre import Monstre


#Création de la fenêtre :

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1000, 800))


bg = pygame.image.load("fond.png")

#game = pygame.Game()
monstre = Monstre()

running = True

#Boucle Infinie
monstre.rect.x = monstre.rect.x + 100
monstre.rect.y = monstre.rect.y + 300
while running:
    ecran.blit(bg, (0, 0))
    ecran.blit(monstre.image,(monstre.rect.x, monstre.rect.y))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("jeu fermé")
        #Mouvements Monstres

        monstre.mouvements()
        #if monstre.rect.