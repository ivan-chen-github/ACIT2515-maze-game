import pygame
from views.tiles import Item

class GameView():
    def __init__(self, walls, goal, items, player, timer, player_sprite):
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
        self._player_sprite = player_sprite
        self._item = Item()
    
    def draw_map(self):
        self._window.fill((50, 25, 0))#-- fills the surface of the game
        text = f"Items obtained: {self._player.backpack}"
        text_surface = self._arial.render(text, True, (255, 255, 255)) #--renders in font arial, and display the items collected
        self._window.blit(text_surface, (0, 500)) #-- displays the message
        #-- draws items at bottom bar once you pick it up
        if self._player.backpack > 0:
            count = 0
            while count < self._player.backpack:
                self._window.blit(self._item.image, (300+50*count, 500))
                count += 1
        #-- draws the objects onto self._window
        self._window.blit(self._player_sprite.image, self._player_sprite.rect)
        self._items.draw(self._window)
        self._walls.draw(self._window)
        self._goal.draw(self._window)
        timer_text = f"Time remaining: {str(round(self._timer, 2))}"
        timer_text_surface = self._arial.render(timer_text, True, (255,255,255))
        self._window.blit(timer_text_surface, (630, 500))
        #-- updates the display
        pygame.display.update()

    def draw_end(self, status, final_score, name, max_name_length):
        NAME_FILLER = "_ "
        self._window.fill((0, 0, 0))
        item_count = f"Items collected: {self._player.backpack}/4"
        if status == True:
            status_text = "You Win!"
        else:
            status_text = "You Lose."
        score_text = f"Final score: {final_score}"
        
        if len(name) == 0:
            display_name = "_ " + NAME_FILLER * (max_name_length-1)
        else:
            display_name = name + NAME_FILLER * (max_name_length-len(name))
        
        prompt_text = f"Enter your name: {display_name}"
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
            self._window.blit(prompt_text_surface, (300, 300))
        self._window.blit(continue_text_surface, (1000-continue_text_surface.get_width(), 550-continue_text_surface.get_height()))
        
        pygame.display.update()

    def draw_scores(self, highscores):
        self._window.fill((0, 0, 0))
        hall_text = f"Hall of Fame"
        continue_text = "Press enter to replay."
        end_text = "Press esc to quit."

        count = 0
        while count < len(highscores) and count <= 6: #-- Display no more than 6 scores
            name_text = highscores[count]['player_name'] #-- recorded name
            name_padding = 12+2*(3-len(name_text)) #-- adds empty spaces
            score_text = str(highscores[count]['score']) #-- recorded score
            score_padding = 28+1*(3-len(score_text)) #-- adds empty spaces
            date_text = highscores[count]['date'] #-- show in format MM-DD

            name_text_surface = self._arial.render(name_text, True, (255, 255, 255)) #--renders in font arial, and display the items collected
            score_text_surface = self._arial.render(score_text, True, (255, 255, 255)) #--renders in font arial, and display the items collected
            date_text_surface = self._arial.render(date_text, True, (255, 255, 255)) #--renders in font arial, and display the items collected

            self._window.blit(name_text_surface, (200, 100+50*count))
            self._window.blit(score_text_surface, (500-score_text_surface.get_width()/2, 100+50*count))
            self._window.blit(date_text_surface, (700, 100+50*count))
            count += 1

        hall_text_surface = self._arial.render(hall_text, True, (255, 255, 255)) #--renders in font arial, and display the items collected
        continue_text_surface = self._small_arial.render(continue_text, True, (255, 255, 255)) 
        end_text_surface = self._small_arial.render(end_text, True, (255, 255, 255)) 
        name_label_surface = self._arial.render("Player", True, (255, 255, 255)) #--renders in font arial, and display the items collected
        score_label_surface = self._arial.render("Score", True, (255, 255, 255)) #--renders in font arial, and display the items collected
        date_label_surface = self._arial.render("Date", True, (255, 255, 255)) #--renders in font arial, and display the items collected


        self._window.blit(hall_text_surface, (500-hall_text_surface.get_width()/2, 0))
        self._window.blit(continue_text_surface, (1000-continue_text_surface.get_width(), 550-continue_text_surface.get_height()))
        self._window.blit(end_text_surface, (0, 550-continue_text_surface.get_height()))

        self._window.blit(name_label_surface, (200, 50))    #-- 3 parts of label are seperated to account for differences in character spacing
        self._window.blit(score_label_surface, (500-score_label_surface.get_width()/2, 50))
        self._window.blit(date_label_surface, (700, 50))

        pygame.display.update()
