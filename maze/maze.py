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
        print(self._layout)

    def check(self, line, col):
        """
        finds empty space or wall based on line number and column number
        param line: description here
        param column: description here
        return: coordinates (line number, column number)
        """

        """ nestedlist[line] by nestedlist[column] is a space (True) or and X (False) """
#        print(self._layout[line])
#        print(self._layout[line][col])
        if self._layout[line][col] == " ":
            return True
        else:
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
        line = random.randint(0, len(self._layout)-1)
        print(line)
        tile = "Here"
        while tile != " ":
            col = random.randint(0, len(self._layout[line])-1)
            print(col)
            tile = self._layout[line][col]
            print(f"tile: {tile}")
        print(line, col, tile)
        return line, col #This returns index, so it's line/col number -1


#Tests
tester = Maze("test.txt")
"""
print("Display")
tester.display()
print("Check")
print(tester.check(1, 1))
"""
print("Random")
temp = tester.find_random_spot()
print(type(temp))