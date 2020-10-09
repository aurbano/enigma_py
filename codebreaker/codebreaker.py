from enigma.rotor import Rotor


class Codebreaker:
    def __init__(self, code: str):
        self.code = code
        self.rotor_count = 3
        self.rotors = [None for x in range(self.rotor_count)]

    def set_rotor(self, index: int, rotor: Rotor):
        self.rotors[index] = rotor
