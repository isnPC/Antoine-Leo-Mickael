import pygame
from random import randint
from Jeu import ecran


class Chauve_souris(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 10
        self.image = pygame.image.load('monstre.png')
        self.bar2vie100 = pygame.image.load('Barre2vie100.png')
        self.bar2vie75 = pygame.image.load('Barre2vie75.png')
        self.bar2vie50 = pygame.image.load('Barre2vie50.png')
        self.bar2vie25 = pygame.image.load('Barre2vie25.png')
        self.bar2vie0 = pygame.image.load('Barre2vie0.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def mouvements(self):
        """Déplace le monstre aléatoirement"""
        self.rect.x += self.velocity
        self.rect.y += self.velocity*randint(-2, 2)

        #-----[Gestion de la sortie d'écran ]-----#

        if self.rect.x < 0:
            self.rect.x = self.rect.x + 1000
        elif self.rect.x > 1000:
            self.rect.x = self.rect.x - 1000
        if self.rect.y < 0:
            self.rect.y = self.rect.y + 2*self.velocity
        elif self.rect.y > 700:
            self.rect.y = self.rect.y - 2*self.velocity

    def attaque_chauve_souris(self):
        if self.rect == player.rect:
            player.health = player.health - self.attack

    def barre2vie(self):
        if self.health == self.max_health:
            ecran.blit(self.bar2vie100, (self.rect.x + 25, self.rect.y +25))
        if self.health == 0.75*self.max_health:
            ecran.blit(self.bar2vie75, (self.rect.x + 25, self.rect.y +25))

