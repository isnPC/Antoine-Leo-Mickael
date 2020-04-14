﻿import pygame
from random import randint


class Chauve_souris(pygame.sprite.Sprite):

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

    def attaque_chauve_souris(self):
        if self.rect == player.rect:
            player.health = player.health - self.attack