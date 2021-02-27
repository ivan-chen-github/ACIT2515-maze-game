class Maze:
    def __init__(self, input_file):
        self._layout = []
        with open(input_file, "r") as in_file:
            self._layout = in_file.read().split("\n")
#        print(self._layout)

    def check(self, line, col):
#        print(self._layout[line])
#        print(self._layout[line][col])
        if self._layout[line][col] == " ":
            return True
        else:
            return False

    def display(self):
        for line in self._layout:
            print(line)


    def find_random_spot(self):
        pass

tester = Maze("test.txt")
print("Display")
tester.display()
print("Check")
print(tester.check(1, 1))
