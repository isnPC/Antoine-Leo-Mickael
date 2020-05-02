import pygame
from random import randint



class Chauve_souris(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 10
        self.image = pygame.image.load('monstre.png')
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

