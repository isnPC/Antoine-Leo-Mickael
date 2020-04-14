import pygame
from Chauve_souris import Chauve_souris
#from glace_chocolat import Glace_chocolat

class Game:


    def spawn_monstres(self):
        all_sprites = pygame.sprite.Group
        for i in range(8):
            mobs = Chauve_souris()
            all_sprites.add(mobs)
            mobs.add(mobs)

