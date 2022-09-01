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
        for i in range(3):
            if self.board[i,0] == self.board[i,1] == self.board[i,2] and self.board != " ":
                return self.board[i,0]
            if self.board[0,i] == self.board[1,i] == self.board[2,i] and self.board != " ":
                return self.board[0,i]
        if self.board[0,0] == self.board[1,1] == self.board[2,2] and self.board != " ":
            return self.board[0,0]
        if self.board[2,0] == self.board[1,1] == self.board[0,2] and self.board != " ":
            return self.board[2,0]
        if np.all(self.board != " "):
            return "d"
        return False