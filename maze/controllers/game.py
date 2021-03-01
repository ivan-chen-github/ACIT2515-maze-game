import pygame
import pygame.locals
from models.maze import Maze
from models.tiles import Item
from models.tiles import Finish
from models.tiles import Wall
from models.player import Player
from controllers.player import PlayerController
from views.game import GameView
from views.player import PlayerView

class GameController():
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
                    self._walls.add(Wall(x*50, y*50))
                if char == "e":
                    self._fin.add(Finish(x*50, y*50))
                    self._invalid_locs.append((x,y))
                if char == "p":
                    self._player.rect.x = x*50
                    self._player.rect.y = y*50
                    self._invalid_locs.append((x,y))   
                

    def place_items(self):
        item_list = []
        item_count = 0
        while item_count < 4:
            loc = self._maze.find_random_spot()
            if loc not in self._invalid_locs:
                self._invalid_locs.append(loc)
                x, y = loc
                self._items.add(Item(x*50, y*50))
                item_count += 1
                print(f"Items created: {item_count}. Location: {loc}")
        print(self._invalid_locs)


    def run(self):

        pygame.init()

        window = pygame.display.set_mode((1000, 1000))
        window.set_colorkey((255, 255, 255))
        clock = pygame.time.Clock()

        self.create_world()
        self.place_items()

        cd = False
        running = True
        while running:
            clock.tick(60)

            for event in pygame.event.get():
                #Click X to quit
                if event.type == pygame.locals.QUIT:
                    running = False

            commands = PlayerController(self._player, self._maze, cd)
            commands.get_input(cd)

            """
            keys = pygame.key.get_pressed()
            if keys[pygame.locals.K_RIGHT] and cd is False:
                player.rect.x = min(player.rect.x + 50, 1000)
                cd = True
            elif keys[pygame.locals.K_LEFT]  and cd is False:
                player.rect.x = max(player.rect.x - 50, 0)
                cd = True
            elif keys[pygame.locals.K_UP] and cd is False:
                player.rect.y = max(player.rect.y - 50, 0)
                cd = True
            elif keys[pygame.locals.K_DOWN] and cd == False:
                player.rect.y = min(player.rect.y + 50, 1000)
                cd = True
            """
            
            
            if pygame.sprite.spritecollide(self._player, self._items, dokill=True):
                self._player._backpack += 1
            if pygame.sprite.spritecollide(self._player, self._fin, dokill=True):
                running = False
            
            
            display = GameView(self._walls, self._fin, self._items, self._player)
            display.draw_map()
        #    window.blit(player.image, player.rect)

            """
            GameController.draw_map()
            PlayerController.draw_map()
            pygame.display.update()
            """

        if self._player._backpack == 4:
            print("Win")
        else:
            print("Lose")

