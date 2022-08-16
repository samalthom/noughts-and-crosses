from sqlalchemy import null


class Piece():
    def __init__(self,type=null):
        self.type = type
        if type == "c":
            self.value = "X"
        elif type == "n":
            self.value = "O"