import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        # Temporarily placing player at top left
        self.rect.x = 0
        self.rect.y = 0
        