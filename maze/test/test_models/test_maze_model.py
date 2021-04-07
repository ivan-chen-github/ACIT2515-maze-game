import pytest
from models.maze import Maze

def test_initialization() :
    """Initializes the maze and test if there is a variable layouts"""
    maze = Maze("../maze.txt")
    assert hasattr(maze, '_layout')

def test_can_move_to():
    ''' Checks if you can move to a certain place on the map '''
    maze = Maze("../maze.txt")
    assert not maze.can_move_to(5,0)
    assert maze.can_move_to (3,2)
    assert maze.can_move_to (5,3)

def test_random_spot():
    """ checks if the maze numbers can return a random number and can move to a open spot"""
    maze = Maze("../maze.txt")
    for num in range(5):
        x,y = maze.find_random_spot()
        assert maze.can_move_to(x,y)
