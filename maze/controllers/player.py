import pygame
from models.player import Player
from models.maze import Maze

class PlayerController():
    def __init__(self, player, maze, clock):
        self._player = player
        self._maze = maze
        self._cd = False
        self._clock = clock
        self._diff = 0

    def get_input(self, time):
        if self._cd is True:
            self.check_cd(time)
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT] and self._cd is False and self._maze.can_move_to((self._player.rect.x+50)/50, self._player.rect.y/50):
            self._player.rect.x = min(self._player.rect.x + 50, 1000)
            self.set_cd()

        elif keys[pygame.locals.K_LEFT]  and self._cd is False and self._maze.can_move_to((self._player.rect.x-50)/50, self._player.rect.y/50):
            self._player.rect.x = max(self._player.rect.x - 50, 0)
            self.set_cd()

        elif keys[pygame.locals.K_UP] and self._cd is False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y-50)/50):
            self._player.rect.y = max(self._player.rect.y - 50, 0)
            self.set_cd()

        elif keys[pygame.locals.K_DOWN] and self._cd == False and self._maze.can_move_to(self._player.rect.x/50, (self._player.rect.y+50)/50):
            self._player.rect.y = min(self._player.rect.y + 50, 1000)
            self.set_cd()


    def set_cd(self):
        self._diff = 0
        self._cd = True
        

    def check_cd(self, time):  
        self._diff += time
        if self._diff >= 1000:
            self._diff = 0
            self._cd = False
