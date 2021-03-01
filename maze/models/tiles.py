import pygame

# Trying to see if I can make everything under this inherit from Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/placeholder.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Item(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('assets/item.png')  

class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('assets/wall.png')

class Finish(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('assets/exit.png')
        
