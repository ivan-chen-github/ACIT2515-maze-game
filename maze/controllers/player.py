import pygame
from models.maze import Maze

class PlayerController():

    TILE_PX = 50 #-- width/height of a tile
    
    def __init__(self, player_sprite, maze):
        """
        Intializes the controller for the player, so you are able to move the player

        :param player: is the play that is in the game
        :type player: Player

        :param maze: is the maze that the player will be in
        :type maze: Maze
        """
        self._player = player_sprite
        self._maze = maze  
        self._cd = {"up": False, "down": False, "left": False, "right": False} #-- movement cooldown. if true, player can not move
        self._time_passed = {"up": 0, "down": 0, "left": 0, "right": 0}  #-- time since player's previous move

    def get_input(self, time):
        """ 
        gets the input from the user, move the player if not on cooldown.
        
        :param time: milliseconds since the last time clock.tick() was called.
        :type time: int
        """
        for key in self._cd:
            if self._cd[key] is True: #-- if player is on cooldown then it will check the time
                self.check_cd(time, key)
        keys = pygame.key.get_pressed() #-- the keys that press
        if keys[pygame.locals.K_RIGHT] and self._cd["right"] is False and self._maze.can_move_to((self._player.rect.x+50)/50, self._player.rect.y/50): #-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.x = min(self._player.rect.x + self.TILE_PX, 1000)
            self.set_cd("right")

        elif keys[pygame.locals.K_LEFT]  and self._cd["left"] is False and self._maze.can_move_to((self._player.rect.x-50)/50, self._player.rect.y/50):#-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.x = max(self._player.rect.x - self.TILE_PX, 0)
            self.set_cd("left")

        elif keys[pygame.locals.K_UP] and self._cd["up"] is False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y-50)/50):#-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.y = max(self._player.rect.y - self.TILE_PX, 0)
            self.set_cd("up")

        elif keys[pygame.locals.K_DOWN] and self._cd["down"] is False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y+50)/50):#-- checks if the they clicked right and if the player can move in the direction
            self._player.rect.y = min(self._player.rect.y + self.TILE_PX, 1000)
            self.set_cd("down")


    def set_cd(self, key):
        """
        sets a movement cooldown and sets time_passed back to zero  

        :param key: the direction
        :type key: str
        """
        self._time_passed[key] = 0
        self._cd[key] = True
        

    def check_cd(self, time, key):  
        """
        Checks if 0.5 seconds has passed since the player's previous move
        
        :param time: milliseconds since the last time clock.tick() was called.
        :type time: int

        :param key: the direction to check
        :type key: str
        """
        self._time_passed[key] += time
        if self._time_passed[key] >= 500:
            self._time_passed[key] = 0
            self._cd[key] = False

    def clear_cd(self, key):
        """
        clears the cooldown for the direction

        :param key: the direction
        :type key: str
        """
        self._cd[key] = False
