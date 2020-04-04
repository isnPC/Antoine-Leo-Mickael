
import pygame


class Monstre(pygame.sprite.Sprite):

    def init(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 10
        self.image = pygame.image.load('Personnage.png')
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.x += self.velocity


