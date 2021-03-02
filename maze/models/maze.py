import random

class Maze:
    """ Initializes the maze by creating a list with and read the maze.txt file

    :param input_file: file the maze will be read from
    :type input_file: str

    :param layout: creates a empty list and puts the maze in layout when reading maze.txt
    :type layout: list
    
    """
    def __init__(self, input_file):
        self._layout = []
        with open(input_file, "r") as in_file:
            self._layout = in_file.read().split("\n")

    def can_move_to(self, col, line):
        """
        Checks if the player can move to the given coordinates
        
        :param line: index of the list that you are selecting from self._layout. Represents y coordinates.
        :type line: int
        
        :param col: index you want from line. Represents x coordinates.
        :type col: int
        
        :returns: True if there is a " " at the coordinates. False if there is a "x" at the coordinates 
        :rtype: bool

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

    def find_random_spot(self):
        """
        finds a random empty space in the maze
        
        :returns: col, line - the coordinates to find a random empty spot in the maze
        :rtype: int, int
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
    