from models.maze import Maze
from models.player import Player

class Game():
    def __init__(self, maze):
        for y, line in maze._layout:
            for x, char in line:
                if char == "x":
                    wall = Item(x, y)





