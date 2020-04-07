import pygame
from random import randint
from player import Player

player = Player()

class Monstre(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5
        self.image = pygame.image.load('monstre.png')
        self.rect = self.image.get_rect()

    def mouvements(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity*randint(-20, 20)
        pygame.time.delay(1000)