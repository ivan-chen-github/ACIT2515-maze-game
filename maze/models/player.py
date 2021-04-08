import pygame

class Player():
    """
    creates the player starting at the top left corner of the screen

    """
    def __init__(self):
        #-- number of items collected
        self._backpack = 0
        