import pygame
import pygame.locals
from models.maze import Maze
from models.tiles import Item
from models.tiles import Finish
from models.tiles import Wall
from models.player import Player
from controllers.player import PlayerController
from views.game import GameView


class GameController():
    TILE_PX = 50

    def __init__(self):
        self._maze = Maze("maze.txt")
        self._invalid_locs = []
        self._items = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._fin = pygame.sprite.Group()
        self._player = Player()


    def create_world(self):
        for y, line in enumerate(self._maze._layout):
            for x, char in enumerate(line):
                if char == "x":
                    self._walls.add(Wall(x*self.TILE_PX, y*self.TILE_PX))
                if char == "e":
                    self._fin.add(Finish(x*self.TILE_PX, y*self.TILE_PX))
                    self._invalid_locs.append((x,y))
                if char == "p":
                    self._player.rect.x = x*self.TILE_PX
                    self._player.rect.y = y*self.TILE_PX
                    self._invalid_locs.append((x,y))   
                

    def place_items(self):
        item_list = []
        item_count = 0
        while item_count < 4:
            loc = self._maze.find_random_spot()
            if loc not in self._invalid_locs:
                self._invalid_locs.append(loc)
                x, y = loc
                self._items.add(Item(x*self.TILE_PX, y*self.TILE_PX))
                item_count += 1

    def run(self):

        pygame.init()
        clock = pygame.time.Clock()

        self.create_world()
        self.place_items()

        cd = False
        commands = PlayerController(self._player, self._maze)

        running = True
        while running:
            time = clock.tick(60)
            for event in pygame.event.get():
                #Click X to quit
                if event.type == pygame.locals.QUIT:
                    running = False
                if event.type == pygame.KEYUP:
                    commands._cd = False
            
            commands.get_input(time)

            if pygame.sprite.spritecollide(self._player, self._items, dokill=True):
                self._player._backpack += 1
            if pygame.sprite.spritecollide(self._player, self._fin, dokill=True):
                running = False

            display = GameView(self._walls, self._fin, self._items, self._player)
            display.draw_map()

        if self._player._backpack == 4:
            print("Win")
        else:
            print("Lose")

