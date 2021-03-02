import pygame
from models.maze import Maze

class PlayerController():

    TILE_PX = 50 #-- width/height of a tile
    
    def __init__(self, player, maze):
        """
        Intializes the controller for the player, so you are able to move the player

        :param player: is the play that is in the game
        :type player: Player

        :param maze: is the maze that the player will be in
        :type maze: Maze
        """
        self._player = player
        self._maze = maze
        self._cd = False    #-- cooldown. if true, player can not move
        self._diff = 0  #-- time since player's previous move

    def get_input(self, time):
        """ 
        gets the input from the user, move the player if not on cooldown.
        
        :param time: milliseconds since the last time clock.tick() was called.
        :type time: int
        """
        if self._cd is True: #-- cd is True then it will check the time
            self.check_cd(time)
        keys = pygame.key.get_pressed() #-- the keys that press
        if keys[pygame.locals.K_RIGHT] and self._cd is False and self._maze.can_move_to((self._player.rect.x+50)/50, self._player.rect.y/50): #-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.x = min(self._player.rect.x + self.TILE_PX, 1000)
            self.set_cd()

        elif keys[pygame.locals.K_LEFT]  and self._cd is False and self._maze.can_move_to((self._player.rect.x-50)/50, self._player.rect.y/50):#-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.x = max(self._player.rect.x - self.TILE_PX, 0)
            self.set_cd()

        elif keys[pygame.locals.K_UP] and self._cd is False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y-50)/50):#-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.y = max(self._player.rect.y - self.TILE_PX, 0)
            self.set_cd()

        elif keys[pygame.locals.K_DOWN] and self._cd == False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y+50)/50):#-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.y = min(self._player.rect.y + self.TILE_PX, 1000)
            self.set_cd()


    def set_cd(self):
        """
        sets a movement cooldown and sets diff back to zero  
        """
        self._diff = 0
        self._cd = True
        

    def check_cd(self, time):  
        """
        Checks if 1 second has passed since the player's previous move
        
        :param time: milliseconds since the last time clock.tick() was called.
        :type time: int
        """
        self._diff += time
        if self._diff >= 1000:
            self._diff = 0
            self._cd = False
