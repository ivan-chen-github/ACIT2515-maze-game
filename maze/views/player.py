import pygame
from models.player import Player

class PlayerView():
    def __init__(self, player):
        self._player = player


    def draw_player(self):
        window.blit(self._player.image, self._player.rect)