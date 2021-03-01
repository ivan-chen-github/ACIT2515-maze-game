import random

class Maze:
    """ Initializes the maze by creating a list with and read the maze.txt file
        
        param layout: creates a empty list and puts the maze in layout when reading maze.txt
        type: list
        
        """
    def __init__(self, input_file):
        self._layout = []
        with open(input_file, "r") as in_file:
            self._layout = in_file.read().split("\n")
    """
    def check(self, line, col):
        # Old checker method

        finds empty space or wall based on line number and column number
        
        param line: is the list that you are selecting from self._layout
        type: int
        
        param col: is the index you want from line
        type: int
        
        return line, col: the coordinates to find the an empty space
        rtype: int, int

        nestedlist[line] by nestedlist[column] is a space (True) or and X (False) 

        if self._layout[line-1][col-1] == " ":      #Assuming the index we pass in starts at 1
            return True
        else:
            return False
    """

    def can_move_to(self, col, line):
        """
        finds empty space or wall based on line number and column number
        
        param line: is the list that you are selecting from self._layout
        type: int
        
        param col: is the index you want from line
        type: int
        
        return: True or False, returns false if there is a "x" located at those coordinates, if there is a " " then returns True as it is empty
        rtype: bool
        
        """
        col = int(col)
        line = int(line)
        try:
            if self._layout[line][col] == "x":      #Assuming we start counting from 0 
                return False
            else:
                return True
        except IndexError:
            return False

    def display(self):
        """
        displays the maze
        """

        # -- for line in nestedlist, for i in line, print i
        for line in self._layout:
            print(line)

    def find_random_spot(self):
        """
        finds a random empty space in the maze
        
        return col, line: the coordinates to find a random empty spot in the maze
        rtype: int, int
        """
        has_spot = False
        while has_spot == False:        # Checks there's a space in the line
            line = random.randint(0, len(self._layout)-1) 
            if " " in self._layout[line]:
                has_spot = True
        tile = "x"
        while tile != " ":
            col = random.randint(0, len(self._layout[line])-1)
            tile = self._layout[line][col]
        return col, line                #This returns index, so it's line/col number -1
    
    def is_item(self):
        pass

    def is_exit(self, line, col):
        """ 
        Exits the game if it the coordinates at line, col are equal to 'e'
        
        param line: is the list that you are selecting from self._layout
        type: int
            
        param col: is the index you want from line
        type: int
            
        return True or False: True if you are at the coordinates with 'e', False if you are not at the coordinates 'e'
        rtype: bool

        """
        if self._layout[line][col] == "e":
            return True
        else:
            return False


#Tests
"""
tester = Maze("maze.txt")
print("Display")
tester.display()
print("Check")
print(tester.check(1, 1))
print("Random index:")
temp = tester.find_random_spot()
print(temp)
"""