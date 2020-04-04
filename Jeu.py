import pygame
pygame.init()
from monstre import Monstre


#Création de la fenêtre :

pygame.display.set_caption("test")
ecran = pygame.display.set_mode((1080, 720))


bg = pygame.image.load("fond.png")

game = Game()
monstre = Monstre()

running = True

#Boucle Infinie

while running:
    for event in pygame.event.get():

        ecran.blit(bg, (0, 0))
        ecran.blit(monstre.image,monstre.rect)
        pygame.display.flip()

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("jeu fermé")
        #Mouvements Monstres

        move()