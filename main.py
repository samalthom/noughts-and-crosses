from game import Game
from game import Human


def run_game(player1=Human(), player2=Human()):
    state = Game()
    print(state.board)
    while not state.winner():
        print(" ")
        print("Cross")
        move = player1.next_move(state)
        state.move(move)
        print(state.board)
        if state.winner() == state.cross:
            print("Player 1 wins!")
            return
        elif state.winner() == "d":
            print("It's a draw.")
            return

        print(" ")
        print("Nought")
        move = player2.next_move(state)
        state.move(move)
        print(state.board)
        if state.winner() == state.cross:
            print("Player 2 wins!")
            return
        elif state.winner() == "d":
            print("It's a draw.")
            return


run_game()
