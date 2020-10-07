from .plug_board import PlugBoard


class Machine:
    def __init__(self):
        self.rotors = []
        self.plug_board = PlugBoard()
        return

    def encode(self, string: str):
        ret = ''
        for char in string:
            ret += self.plug_board.encode(char)

        return ret
