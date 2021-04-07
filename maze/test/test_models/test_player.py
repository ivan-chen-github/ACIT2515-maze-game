import pytest
import pygame
from models.player import Player

def test_create_player():
    player1 = Player()
    assert hasattr(player1,'image')
    assert hasattr(player1,'rect')
    assert hasattr(player1,'rect.x')
    assert hasattr(player1,'rect.y')
    assert hasattr(player1, '_backpack')
