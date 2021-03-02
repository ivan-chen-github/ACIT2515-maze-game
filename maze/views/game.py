import pygame

class GameView():
    def __init__(self, walls, fin, items, player):
        """
        Initializes the Gameview in order to view the maze
        
        param arial: creates the font arial with the font 45
        type: pygame.font.Font

        param walls: the group of walls
        type: pygame.sprite.Group

        param fin:  the group of finish
        type: pygame.sprite.Group

        param items: the group of items
        type: pygame.sprite.Group

        param player: is the player in the game
        type: Player

        """
        self._arial = pygame.font.SysFont('arial', 45)
        self._walls = walls
        self._fin = fin
        self._items = items
        self._player = player
        self._window = pygame.display.set_mode((1000, 1050)) #-- is the size of the screen for the maze
        self._window.set_colorkey((255, 255, 255)) #-- sets the transparency

    def draw_map(self):
        self._window.fill((50, 25, 0))#-- fills the surface of the game
        text = f"Items obtained: {self._player._backpack}"
        text_surface = self._arial.render(text, True, (255, 255, 255)) #--renders in font arial, and display the items collected
        self._window.blit(text_surface, (0, 1000)) #-- displays the message

        #-- draws the objects onto self._window
        self._window.blit(self._player.image, self._player.rect)
        self._items.draw(self._window)
        self._walls.draw(self._window)
        self._fin.draw(self._window)

        #-- updates the display
        pygame.display.update()
