import pygame

class GameView():
    def __init__(self, walls, goal, items, player, timer):
        """
        Initializes the Gameview in order to view the maze
        
        :param arial: creates the font arial with the font 45
        :type arial: pygame.font.Font

        :param walls: the group of walls
        :type walls: pygame.sprite.Group

        :param goal:  the group of goal. It will only have the exit.
        :type goal: pygame.sprite.Group

        :param items: the group of items
        :type items: pygame.sprite.Group

        :param player: is the player in the game
        :type player: Player

        """
        self._arial = pygame.font.SysFont('arial', 45)
        self._walls = walls
        self._goal = goal
        self._items = items
        self._player = player
        self._window = pygame.display.set_mode((1000, 550)) #-- is the size of the screen for the maze. currently assumes 20 tiles across and 10 tiles down.
        self._window.set_colorkey((255, 255, 255)) #-- sets the transparency
        self._timer = timer
    def draw_map(self):
        self._window.fill((50, 25, 0))#-- fills the surface of the game
        text = f"Items obtained: {self._player._backpack}"
        text_surface = self._arial.render(text, True, (255, 255, 255)) #--renders in font arial, and display the items collected
        self._window.blit(text_surface, (0, 500)) #-- displays the message

        #-- draws the objects onto self._window
        self._window.blit(self._player.image, self._player.rect)
        self._items.draw(self._window)
        self._walls.draw(self._window)
        self._goal.draw(self._window)
        timer_text = self._arial.render(str(round(self._timer, 2)), True, (255,255,255))
        self._window.blit(timer_text, (900, 500))
        #-- updates the display
        pygame.display.update()
