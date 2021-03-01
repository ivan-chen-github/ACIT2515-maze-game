import pygame
from models.player import Player
from models.maze import Maze

class PlayerController():
    def __init__(self, player, maze, cd):
        self._player = player
        self._maze = maze
        self._cd = cd

    def get_input(self, cd):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                cd = False
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT] and self._cd is False and self._maze.can_move_to((self._player.rect.x+50)/50, self._player.rect.y/50):
            self._player.rect.x = min(self._player.rect.x + 50, 1000)
            return  True
        elif keys[pygame.locals.K_LEFT]  and self._cd is False and self._maze.can_move_to((self._player.rect.x-50)/50, self._player.rect.y/50):
            self._player.rect.x = max(self._player.rect.x - 50, 0)
            return  True
        elif keys[pygame.locals.K_UP] and self._cd is False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y-50)/50):
            self._player.rect.y = max(self._player.rect.y - 50, 0)
            return  True
        elif keys[pygame.locals.K_DOWN] and self._cd == False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y+50)/50):
            self._player.rect.y = min(self._player.rect.y + 50, 1000)
            return  True

        
