class Piece():
    def __init__(self,type=None):
        self.type = type
        if type == "c":
            self.value = "X"
        elif type == "n":
            self.value = "O"