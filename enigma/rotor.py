class Rotor:
    def __init__(self, config: str, notch: str = None):
        self.config = config
        self.notch = notch
        self.position = 0

    def set_position(self, position: int):
        self.position = position

    def get(self, char: str):
        # return encoded char + whether the next rotor should rotate
        return char
