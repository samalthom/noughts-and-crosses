from game import Game
from player import Human

import numpy as np

def run_game(player1=Human(), player2=Human()):
    state = Game()
    while not state.winner():
        move = player1.next_move()
        state.move(move)
        move = player2.next_move()
        state.move(move)
