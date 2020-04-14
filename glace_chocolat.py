import pygame


player = Player()

class Glace_chocolat(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5
        self.image = pygame.image.load('chocolat.png')
        self.rect = self.image.get_rect()

    def mouvements(self):
        equart_x = player.rect.x - self.rect.x
        if equart_x < 0:
            self.rect.x = self.rect.x - self.velocity
        else:
            self.rect.x = self.rect.x + self.velocity

        equart_y = player.rect.y - self.rect.y
        if equart_y < 0:
            self.rect.y = self.rect.y + self.velocity
        else:
            self.rect.y = self.rect.y - self.velocity

        pygame.time.delay(1000)

    def attaque_glace_chocolat(self):
        if self.rect == player.rect:
            player.health = player.health - self.attack