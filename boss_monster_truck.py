import pygame

class Monster_Truck(pygame.sprite.Sprite):

    def __init__(self, x ,y):
        super().__init__()
        self.health = 1000
        self.max_health = 1000
        self.attack = 20
        self.velocity = 1
        self.image = pygame.image.load('monster_truck.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def boss_mouvements(self):
        self.rect = self.rect + 2*self.velocity