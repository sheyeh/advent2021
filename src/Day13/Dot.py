class Dot:
    def __init__(self, input_str):
        coords = input_str.rstrip().split(",")
        self.x = int(coords[0])
        self.y = int(coords[1])

    def __str__(self):
        return "<{},{}>".format(self.x, self.y)

    def __eq__(self, other):
        return other and self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 10000 + self.y

    def fold(self, instruction):
        folding_line = instruction[1]
        if instruction[0] == "x" and self.x > folding_line:
            self.x = folding_line - (self.x - folding_line)
        else:
            if instruction[0] == "y" and self.y > folding_line:
                self.y = folding_line - (self.y - folding_line)
        return self
