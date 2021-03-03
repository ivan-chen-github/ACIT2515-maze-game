import pygame

# Trying to see if I can make everything under this inherit from Tile class
class Tile(pygame.sprite.Sprite):
    """
    Tile is the class the represent a square in the game

    :param x: x is the coordinate that it will be placed in the game 
    :type x: int

    :param y: y is the coordinate that it will place a tile on the y axis in the game
    :type y: int

    """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/placeholder.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Item(Tile):
    """
    Represents collectable items.
    Item will load the item image in the game, that is placed on coordinate (x,y), inherits attribute from tile

    :param x: x is the coordinate that it will be placed in the game 
    :type x: int

    :param y: y is the coordinate that it will place a tile on the y axis in the game
    :type y: int
    
    """
    def __init__(self, x, y):
        super().__init__(x, y) #-- sets the value x,y value in parent class Tile
        self.image = pygame.image.load('assets/item.png')  #--loads the item image

class Wall(Tile):
    """
    Represents and impassable wall.
    Wall will load the item image in the game, that is placed on coordinate (x,y), inherits attribute from tile

    :param x: x is the coordinate that it will be placed in the game 
    :type x: int

    :param y: y is the coordinate that it will place a tile on the y axis in the game
    :type y: int
    
    """
    def __init__(self, x, y):
        super().__init__(x, y)#-- sets the value x,y value in parent class Tile
        self.image = pygame.image.load('assets/wall.png')#--loads the item image

class Goal(Tile):
    """
    Represents the goal/exit.
    Goal will load the item image in the game, that is placed on coordinate (x,y), inherits attribute from tile

    :param x: x is the coordinate that it will be placed in the game 
    :type x: int

    :param y: y is the coordinate that it will place a tile on the y axis in the game
    :type y: int
    
    """
    def __init__(self, x, y):
        super().__init__(x, y)#-- sets the value x,y value in parent class Tile
        self.image = pygame.image.load('assets/exit.png')#--loads the item image
        