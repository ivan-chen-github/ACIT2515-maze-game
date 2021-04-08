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
        self._small_arial = pygame.font.SysFont('arial', 20)
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

    def draw_end(self, status, final_score, name):
        self._window.fill((0, 0, 0))
        item_count = f"Items collected: {self._player._backpack}/4"
        if status == True:
            status_text = "You Win!"
        else:
            status_text = "You Lose."
        score_text = f"Final score: {final_score}"
        prompt_text = f"Enter your name: {name}"
        continue_text = "Press enter to continue."

        item_count_surface = self._arial.render(item_count, True, (255, 255, 255)) #--renders in font arial, and display the items collected
        status_text_surface = self._arial.render(status_text, True, (255, 255, 255))
        score_text_surface = self._arial.render(score_text, True, (255, 255, 255))
        prompt_text_surface = self._arial.render(prompt_text, True, (255, 255, 255))
        continue_text_surface = self._small_arial.render(continue_text, True, (255, 255, 255))


        self._window.blit(item_count_surface, (500-item_count_surface.get_width()/2, 200))
        self._window.blit(status_text_surface, (500-status_text_surface.get_width()/2, 150))
        if status == True:
            self._window.blit(score_text_surface, (500-score_text_surface.get_width()/2, 250))
            self._window.blit(prompt_text_surface, (500-prompt_text_surface.get_width()/2, 300))
        self._window.blit(continue_text_surface, (1000-continue_text_surface.get_width(), 550-continue_text_surface.get_height()))
        
        pygame.display.update()

    def draw_final(self):
        self._window.fill((0, 0, 0))
        item_count = f"Hall of Fame"
        continue_text = "Press any key to replay."

        item_count_surface = self._arial.render(item_count, True, (255, 255, 255)) #--renders in font arial, and display the items collected
        continue_text_surface = self._small_arial.render(continue_text, True, (255, 255, 255))

        self._window.blit(item_count_surface, (500-item_count_surface.get_width()/2, 0))
        self._window.blit(continue_text_surface, (1000-continue_text_surface.get_width(), 550-continue_text_surface.get_height()))
        
        pygame.display.update()