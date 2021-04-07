Maze Game

Project Background:                                                                                   
This project involves programming a maze-like game using Python and Pygame. The game focuses on
a player controlled sprite (using arrow keys) which can navigate the maze to collect items and 
reach the goal. The maze structure is generated from a text file and items are randomly placed 
on empty coordinates within the maze. The player wins by collecting all four randomly placed items
and then reaching the goal (symbolized by the Door in the maze).

A second feature of the project is to save and display scores from the game onto a web page. The web page 
served from a Flask server which is also run on the local machine. After a player wins the game, their 
score is sent to the Flask server, which in turn will appear on the web page after refreshing the page.


Team Members:                                                                       
Ivan Chen       - UI and Game Logic Programming                                                       
Brandley Gee    - Code Documentation and Unit Testing                                            
Arshia Aryanfar - Debugging and Data Handling                                                      
Edward To       - Web API and Asset Management                                       


Project Structure:                                                                                   
assignment_demo                                                                                         
|-README.md                                                                                        
|-documentation                                                                                         
|---|-uml.pdf                                                                                                      
|-flask                                                                                                                  
|---|-app.py                                                                                                                              
|---|-scores.json                                                                                                     
|---|-templates                                                                                               
|------|-index.html                                                                                                              
|---|-models                                                                                                     
|------|-score.py                                                                                                      
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
|------|-score.py                                                                                                       
|------|-score_manager.py                                                                                       
|---|-views                                                                                            
|------|-__init__.py                                                                                   
|------|-game.py                                                                                   


Required Libraries:                                                                                  
Since this game relies on Pygame modules, Pygame must be installed to run the game. Pygame can be
installed using the command "pip install pygame" in the terminal. Flask is required to run the web api 
which hosts the scores on a webpage. Flask can be installed using the command "pip install Flask".

Running the Flask server:                                                                                      
To start the server, navigate to the "assignment_demo\flask" directory and run the command "python app.py"
in the terminal. The web page can be accessed from your browser with the local url http://127.0.0.1:5000

Running the game:                                                                                    
To run the game, navigate to the "assignment_demo\maze" directory and run the command "python main.py"
in the terminal. 
The maze layout is defined in "maze.txt" in the same directory. Walls are represented by "x", pathways
by " ", the player's starting location by "p", and the exit by "e".


Game Controls:                                                                                         
Moving the sprite 	- Use the arrow keys to move the player sprite.                                          
Collecting items  	- Move the sprite on top of an item to collect it.                                        
Winning the game 	- Win by collecting all 4 items (Jewels) before reaching the exit (Door). Reaching    
                          the exit without collecting all the items will result in a loss.                  
Exiting the game  	- Reach the Door to exit the game or click the X                                       




