import pygame
import random


"""
# Trying to see if I can make everything under this inherit from Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ""
        self.rect = self.image.get_rect()
        # Temporarily randomly placing items, not checking if it's a space
        self.rect.x = x
        self.rect.y = y
"""

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/item.png')
        self.rect = self.image.get_rect()
        # Temporarily randomly placing items, not checking if it's a space
        self.rect.x = x
        self.rect.y = y

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/wall.png')
        self.rect = self.image.get_rect()
        # Temporarily randomly placing items, not checking if it's a space
        self.rect.x = x
        self.rect.y = y

class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/exit.png')
        self.rect = self.image.get_rect()
        # Temporarily randomly placing items, not checking if it's a space
        self.rect.x = x
        self.rect.y = y