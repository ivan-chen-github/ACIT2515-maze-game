Maze Game

Project Background:                                                                                   
This project involves programming a maze-like game using Python and Pygame. The game focuses on
a player controlled sprite (using arrow keys) which can navigate the maze to collect items and 
reach the goal. The maze structure is generated from a text file and items are randomly placed 
on empty coordinates within the maze. The player wins by collecting all four randomly placed items
and then reaching the goal (symbolized by the Door in the maze).


Team Members:                                                                       
Ivan Chen       - UI and Game Logic Programming                                                       
Brandley Gee    - Code Documentation and App Programming                                            
Arshia Aryanfar - App Programming and Data Handling                                                      
Edward To       - Project Management and Asset Preparation                                              


Project Structure:                                                                                   
assignment_demo                                                                                         
|-README.md                                                                                        
|-documentation                                                                                         
|---|-uml.pdf                                                                                            
|-maze                                                                                                    
|---|-main.py                                                                                               
|---|-maze.txt                                                                                             
|---|-assets                                                                                              
|---|-controllers                                                                                        
|------|-__init__.py                                                                                  
|------|-game.py                                                                                          
|------|-player.py                                                                                    
|---|-models                                                                                           
|------|-__init__.py                                                                                 
|------|-maze.py                                                                                       
|------|-player.py                                                                                   
|------|-tiles.py                                                                                     
|---|-views                                                                                            
|------|-__init__.py                                                                                   
|------|-game.py                                                                                   


Required Libraries:                                                                                  
Since this game relies on Pygame modules, Pygame must be installed to run the game. Pygame can be
installed using the command "pip install pygame" in the terminal.


Running the game:                                                                                    
To run the game, navigate to the "assignment_demo\maze" directory and run the command "python main.py"
in the terminal. 
The maze layout is defined in "maze.txt" in the same directory. Walls are represented by "x", pathways
by " ", the player's starting location by "p", and the exit by "e".


Game Controls:                                                                                         
Moving the sprite 	- Use the arrow keys to move the player sprite.
Collecting items  	- Move the sprite on top of an item to collect it.
<<<<<<< HEAD
Winning the game 	- Win by collecting all 4 items (Jewels) before reaching the exit (door). 
=======
Winning the game 	- Win by collecting all 4 items (Jewels) before reaching the exit (Door). 
>>>>>>> 836da2f4fa9a03da816f11c0bc59c127d6228b1c
					  Reaching the exit without collecting all the items will result in a loss.
Exiting the game  	- Reach the Door to exit the game or click the X




