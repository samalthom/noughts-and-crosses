from pieces import Piece
import numpy as np

class Board(Piece):
    def __init__(self, size=3, first="c"):
        self.size = size
        self.first = first
        self.board = np.zeroes(3,3)