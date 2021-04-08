import pygame
import pygame.locals
import requests
import json
from models.maze import Maze
from models.tiles import Item
from models.tiles import Goal
from models.tiles import Wall
from models.player import Player
from models.score import Score
from controllers.player import PlayerController
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
        self._player = Player()# -- creates a player


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
                    self._player.rect.x = x*self.TILE_PX
                    self._player.rect.y = y*self.TILE_PX
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

    def run(self):
        """ 
        The method that will run the application

        Will run until you reach the goal, where it will tell you if you lose or win
        """
        pygame.init()
        clock = pygame.time.Clock()

        #-- creates the maze with the items
        self.create_world()
        self.place_items()

        cd = False
        commands = PlayerController(self._player, self._maze) #-- intializes the player controller

        running = True
        end_screen = False #-- shows game over screen if true
        final_screen = False #-- shows high scores if true
        total_keypress = 0
        clock = pygame.time.Clock()
        timer = 20
        final_score = 0
        name = "_ _ _" #-- this is what the player's name
        name_length = 0 #-- length of player's name

        while running:
            time = clock.tick(60) #-- 60 frames at most per second
            for event in pygame.event.get(): #-- gets the input of your keyboard
                if event.type == pygame.locals.QUIT:
                    running = False

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

            if pygame.sprite.spritecollide(self._player, self._items, dokill=True): #-- if the player gets to the item add to backpack
                self._player._backpack += 1
            if pygame.sprite.spritecollide(self._player, self._goal, dokill=True): #-- if the player reaches the end then stop running the game
                """
                DEBUG PURPOSES ONLY
                """                
#                self._player._backpack = 4
                if self._player._backpack == 4: #-- if the backpack has four in it, then you win

                    key_diff = total_keypress - 33 #-- find the difference of total keypress and fewest possible keypresses (33)
                    final_score = 100 - key_diff #-- final score out of 100 based on extra keypresses past 33
                    """
                    print(f"\nItems collected: {self._player._backpack}/4.\nYou Win!")
                    print(f"Final Score: {final_score}")
                    """
                    game_won = True
                else:
                    """
                    final_score = 0
                    print(f"\nItems collected: {self._player._backpack}/4.\nYou Lose.")
                    print(f"Final Score: {final_score}")
                    """
                    game_won = False
                end_screen = True
            timer = timer - (time/1000)  
            if timer <= 0:
                """
                final_score = 0
                print(f"\nItems collected: {self._player._backpack}/4.\nYou Lose.")
                print(f"Final Score: {final_score}")
                """
                game_won = False
                end_screen = True
            display = GameView(self._walls, self._goal, self._items, self._player, timer) 
            display.draw_map() #-- displays the maze and player

            
            while end_screen == True: #-- Display game over screen
                time = clock.tick(60) #-- 60 frames at most per second
                for event in pygame.event.get(): #-- gets the input of your keyboard
                    if event.type == pygame.locals.QUIT:
                        running = False
                        end_screen = False
                    if event.type == pygame.KEYDOWN:
                        if name_length <= 3:
                            if (event.key == pygame.K_BACKSPACE):
                                if name_length >= 1:
                                    if name_length == 3:
                                        name = name[0:4] + "_"
                                    elif name_length == 2:
                                        name = name[0:2] + "_ _"
                                    elif name_length == 1:
                                        name = "_ _ _"
                                    name_length -= 1
                            elif (event.key == pygame.K_RETURN): #-- player submits their name
                                true_name = "" #-- unformatted name to be stored
                                count = 0
                                while count < name_length:
                                    true_name += name[count*2]
                                    count += 1
                                score_record = Score(true_name, final_score)
                                json_score = json.dumps(score_record.__dict__)
                                response = requests.put("http://127.0.0.1:5000/score", json=json_score, headers={"Content-type": "application/json"})
                                #-- send score to Flask server

                                end_screen = False
                                final_screen = True
                            else:
                                if type(event.unicode) is str and event.unicode != "":
                                    if name_length == 0:
                                        name = event.unicode.upper() + name[1:]
                                        name_length += 1
                                    elif name_length == 1:
                                        name = name[:2] + event.unicode.upper() + name[3:]
                                        name_length += 1
                                    elif name_length == 2:
                                        name = name[:4] + event.unicode.upper()
                                        name_length += 1

                display.draw_end(game_won, final_score, name)
            

            while final_screen == True:
                for event in pygame.event.get():
                    if event.type == pygame.locals.QUIT:
                        running = False
                        final_screen = False
                    if event.type == pygame.KEYDOWN:
                        running = False
                        final_screen = False
                        return True
                
                """
                code to get scores from json
                """

                display.draw_final()


            


