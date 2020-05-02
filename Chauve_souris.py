import pygame
from random import randint




class Chauve_souris(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 10
        self.image = pygame.image.load('monstre.png')
        self.rect = self.image.get_rect()

    def mouvements(self):
        rectPrecedent = self.image.get_rect()
        self.rect.x += self.velocity
        self.rect.y += self.velocity*randint(-5, 5)

        #-----[Gestion de la sortie d'écran ]-----#

        if self.rect.x < 0 or self.rect.x > 1000:
            self.rect = (5, 500)
        elif self.rect.y < 0 or self.rect.y > 800:
            self.rect = rectPrecedent

        #-----------------------------------------#

        pygame.time.delay(500)
        return self.rect

    def attaque_chauve_souris(self):
        if self.rect == player.rect:
            player.health = player.health - self.attack

