import pygame
import pygame.locals
import requests
import json
from models.maze import Maze
from models.player import Player
from models.score import Score
from models.score_manager import ScoreManager
from controllers.player import PlayerController
from views.tiles import Item
from views.tiles import Goal
from views.tiles import Wall
from views.player import PlayerView
from views.game import GameView


class GameController():
    """ 
    This is the class that will outline the maze.

    Interacts with the player controller
 
    """
    TILE_PX = 50 #-- width/height of a tile

    def __init__(self):
        self._maze = Maze("maze.txt") #-- creates a maze object, and loads the maze outline
        self._invalid_locs = [] #-- list of places an item can be placed. Can not be on player, exit, or another item.
        self._items = pygame.sprite.Group() # -- create items in sprite group
        self._walls = pygame.sprite.Group() # -- create items in sprite group
        self._goal = pygame.sprite.Group() # -- create items in sprite group
        self._player = Player() # -- creates a player
        self._player_sprite = PlayerView() #-- player's sprite
        self._running = True

    def create_world(self):
        """ creates the maze by adding the walls, the player, and the goal """
        for y, line in enumerate(self._maze._layout): #--loops through the lines in the maze
            for x, char in enumerate(line):  #-- loops throught the chars in the line
                if char == "x": #-- if it is an "x" then add the wall at the location
                    self._walls.add(Wall(x*self.TILE_PX, y*self.TILE_PX))
                if char == "e": #-- if it is an "e" add the exit at the location
                    self._goal.add(Goal(x*self.TILE_PX, y*self.TILE_PX))
                    self._invalid_locs.append((x,y))
                if char == "p": #-- if it is a p add the player at the location
                    self._player_sprite.rect.x = x*self.TILE_PX
                    self._player_sprite.rect.y = y*self.TILE_PX
                    self._invalid_locs.append((x,y))   
    
    def place_items(self):
        """ finds a random spot in the maze that is empty and adds the item """
        item_list = []
        item_count = 0
        while item_count < 4: #-- makes sure that there are four items in the maze
            loc = self._maze.find_random_spot() #-- finds the random spot
            if loc not in self._invalid_locs:  #-- checks the item doesn't spawn on the play, exit, or another item
                self._invalid_locs.append(loc) #-- marks the location as invalid for next item spawn
                x, y = loc
                self._items.add(Item(x*self.TILE_PX, y*self.TILE_PX)) #-- adds the item to the maze
                item_count += 1

    def end_screen(self, display, game_won, final_score):
        """
        runs the logic for the game over screen

        :param display: the display initialized in run()
        :type display:

        :param game_won: true if player won the game, false if lost
        :type game_won: bool
        
        :param final score: the player's final score
        :type final score: int

        :return: true if we want to go to high score screen, false otherwise
        :rtype: bool
        """
        MAX_NAME_LENGTH = 5
        name = ""
        end_screen = True
        while end_screen: #-- Display game over screen
            for event in pygame.event.get(): #-- gets the input of your keyboard
                if event.type == pygame.locals.QUIT:
                    self._running = False
                    end_screen = False
                    return False #-- Do not go to score screen
                if event.type == pygame.KEYDOWN:
                    if len(name) <= MAX_NAME_LENGTH:
                        if (event.key == pygame.K_BACKSPACE) and len(name) >= 1: #-- deletes most recent character
                            name = name[:len(name)-1]
                        elif (event.key == pygame.K_RETURN): #-- player submits their name
                            score_record = Score(name, final_score)
                            json_score = json.dumps(score_record.__dict__)
                            response = requests.put("http://127.0.0.1:5000/score", json=json_score, headers={"Content-type": "application/json"})
                            #-- send score to Flask server
                            end_screen = False
                            score_screen = True
                            return True #-- Go to score screen

                        elif type(event.unicode) is str and len(name) < MAX_NAME_LENGTH: #-- Adds key input to name
                            name = name + event.unicode.upper()

            display.draw_end(game_won, final_score, name, MAX_NAME_LENGTH)

    def score_screen(self, display):
        """
        Runs the logic for the score screen.

        :param display: The display initialized in run()
        :type display:

        :return: true if we want to replay the game, false otherwise
        :rtype: bool
        """
        score_screen = True
        highscores = ScoreManager()
        highscores = highscores.from_json("http://127.0.0.1:5000/json")
        sorted_list = sorted(highscores, key=lambda k: k["score"], reverse=True) #-- sort all recorded scores by highest score

        while score_screen:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    score_screen = False
                    self._running = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE): #-- Pressing esc key closes game
                        score_screen = False
                        return False #-- quit
                    elif (event.key == pygame.K_RETURN): #-- Pressing enter key restarts game
                        score_screen = False
                        return True #-- replay
            display.draw_scores(sorted_list) #-- Draw high score screen

    
    def run(self):
        """ 
        The method that will run the application

        Will run until you reach the goal, where it will tell you if you lose or win
        
        :return: true if player decides to replay, false otherwise
        :rtype: bool
        """
        pygame.init()
        clock = pygame.time.Clock()

        #-- creates the maze with the items
        self.create_world()
        self.place_items()

        commands = PlayerController(self._player_sprite, self._maze) #-- intializes the player controller

        end_screen = False #-- shows game over screen if true
        score_screen = False #-- shows high scores if true
        total_keypress = 0 #-- used to calculate score
        clock = pygame.time.Clock()
        timer = 20 #-- You have 20 seconds to complete the game
        final_score = 0
        

        while self._running:
            time = clock.tick(60) #-- 60 frames at most per second
            timer = timer - (time/1000)

            for event in pygame.event.get(): #-- gets the input of your keyboard
                if event.type == pygame.locals.QUIT:
                    self._running = False
                if event.type == pygame.KEYUP:
                    total_keypress += 1 #-- count number of keypresses
                    #-- sets removes movement cooldown every time the key is released
                    if (event.key == pygame.K_UP):
                        action = "up"
                        commands._cd[action] = False
                        commands._time_passed[action] = 0
                    if (event.key == pygame.K_DOWN):
                        action = "down"
                        commands._cd[action] = False
                        commands._time_passed[action] = 0
                    if (event.key == pygame.K_LEFT):
                        action = "left"
                        commands._cd[action] = False
                        commands._time_passed[action] = 0
                    if (event.key == pygame.K_RIGHT):
                        action = "right"
                        commands._cd[action] = False
                        commands._time_passed[action] = 0

            commands.get_input(time)

            if pygame.sprite.spritecollide(self._player_sprite, self._items, dokill=True): #-- if the player gets to the item add to backpack
                self._player.backpack += 1
            if pygame.sprite.spritecollide(self._player_sprite, self._goal, dokill=True): #-- if the player reaches the end then stop running the game

                if self._player.backpack == 4: #-- if the backpack has four in it, then you win
                    key_diff = total_keypress - 33 #-- find the difference of total keypress and fewest possible keypresses (33)
                    final_score = 100 - key_diff #-- final score out of 100 based on extra keypresses past 33
                    game_won = True
                else:
                    game_won = False
                end_screen = True

            if timer <= 0:
                game_won = False
                end_screen = True
            display = GameView(self._walls, self._goal, self._items, self._player, timer, self._player_sprite) 
            display.draw_map() #-- displays the maze and player
            
            if end_screen:
                score_screen = self.end_screen(display, game_won, final_score) #-- true is end_screen exits properly

            if score_screen: #-- Get the saved high scores before going to score screen
                replay = self.score_screen(display)
                self._running = False
                return replay
        
    

