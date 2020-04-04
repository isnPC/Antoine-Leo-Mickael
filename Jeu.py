import pygame
pygame.init()
from monstre import Monstre


#Création de la fenêtre :

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1080, 720))


bg = pygame.image.load("fond.png")

#game = pygame.Game()
monstre = Monstre()

running = True

#Boucle Infinie

while running:
    ecran.blit(bg, (0, 0))
    ecran.blit(monstre.image,monstre.rect)
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("jeu fermé")
        #Mouvements Monstres
        if event.type  == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            monstre.move()