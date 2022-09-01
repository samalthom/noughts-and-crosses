import numpy as np

class Game():
    def __init__(self):
        self.cross = "X"
        self.nought = "O"
        self.board = np.full((3, 3), " ")

        self.next_player = self.cross
        self.swap_player = {self.cross:self.nought,self.nought:self.cross}

    def valid(self,row,col):
        return self.board(row,col) == " "

    def move(self,move):
        row = move[0]
        col = move[1]
        if self.valid(row,col):
            self.board[row,col] = self.next_player
        return self.board
    
    def winner(self):
        return False