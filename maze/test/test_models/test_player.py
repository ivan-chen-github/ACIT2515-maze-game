import pytest
import pygame
from models.player import Player

def test_create_player():
    """
    check player has attribute backpack and it is an int
    """
    player1 = Player()
    assert hasattr(player1, 'backpack')
    assert type(player1.backpack) is int
