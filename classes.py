class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vie = 100
        self.degats = 10
        self.image = pygame.image.load('assets/Unknown.png')
        #il faudras changer l'image pour mettre la vrai image du joueur.
        self.rect = self.image.get_rect()
