import random

class Maze:
    def __init__(self, input_file):
        """
        code documentation goes here
        """

        """ function that reads maze.txt and creates nested list? """
        self._layout = []
        with open(input_file, "r") as in_file:
            self._layout = in_file.read().split("\n")
    """
    def check(self, line, col):
        # Old checker method

        finds empty space or wall based on line number and column number
        param line: description here
        param column: description here
        return: coordinates (line number, column number)
        

        nestedlist[line] by nestedlist[column] is a space (True) or and X (False) 

        if self._layout[line-1][col-1] == " ":      #Assuming the index we pass in starts at 1
            return True
        else:
            return False
    """

    def can_move_to(self, line, col):
        """
        finds empty space or wall based on line number and column number
        param line: description here
        param column: description here
        return: coordinates (line number, column number)
        

        nestedlist[line] by nestedlist[column] is a space (True) or and X (False) 
        """
        line = int(line)
        col = int(col)
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
        code documentation
        """

        """ for line in nestedlist, for i in line, print i """
        for line in self._layout:
            print(line)

    def find_random_spot(self):
        """
        finds a random empty space in the maze
        code documentation
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