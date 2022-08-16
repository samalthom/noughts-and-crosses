from pieces import Piece

class Board(Piece):
    def __init__(self, size=3, first="c"):
        self.size = size
        self.first = first
        if first == "c":
            self.crosses = 5
            self.noughts = 4
        else:
            self.noughts = 5
            self.crosses = 4