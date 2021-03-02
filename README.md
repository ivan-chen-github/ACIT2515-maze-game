Maze Game

Project Background:                                                                                   
This project involves programming a maze-like game using Python and Pygame. The game focuses on
a player controlled sprite (using arrow keys) which can navigate the maze to collect items and 
reach the goal. The maze structure is generated from a text file and items are randomly placed 
on empty coordinates within the maze. The player wins by collecting all four randomly placed items
and then reaching the goal (symbolized by the heart item in the maze).


Team Members:                                                                      
Ivan Chen       - UI and Game Logic Programming
Brandley Gee    - Code Documentation and App Programming
Arshia Aryanfar - App Programming and Data Handling
Edward To       - Project Management and Asset Preparation

Project Structure:
assignment_demo
|-README.md
|-documentation
   |-uml.pdf
|-maze
   |-main.py
   |-maze.txt
   |-assets
   |-controllers
      |-__init__.py
      |-game.py
      |-player.py
   |-models
      |-__init__.py
      |-maze.py
      |-player.py
      |-tiles.py
   |-views
      |-__init__.py
      |-game.py


Required Libraries:
Since this game relies on Pygame modules, Pygame must be installed to run the game. Pygame can be
installed using the command "pip install pygame" in the terminal.


Running the game:
To run the game, browse to the "assignment_demo\maze" folder and run the command "python main.py"
in the terminal.


Game Controls:
Moving the sprite - Arrow Keys
Collecting items  - Move the sprite on top of the item to collect it
Exiting the game  - Collect the Heart item to exit the game or click the X




