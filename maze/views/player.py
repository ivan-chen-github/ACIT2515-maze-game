import pygame

class PlayerView(pygame.sprite.Sprite):
    """
    creates the player starting at the top left corner of the screen

    """
    def __init__(self):
        super().__init__()
        #-- loads the player image
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        # --placing player at top left
        self.rect.x = 0
        self.rect.y = 0

        