import pygame
from random import randint


class Chauve_souris(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5
        self.image = pygame.image.load('monstre.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def mouvements(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity*randint(-20, 20)

    def attaque_chauve_souris(self):
        if self.rect == player.rect:
            player.health = player.health - self.attack