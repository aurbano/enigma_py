from typing import List
from .rotor import Rotor
from .plug_board import PlugBoard
from .plug_lead import PlugLead


class Machine:
    def __init__(self, rotors: List[Rotor], reflector: Rotor):
        self.rotors = rotors
        self.reflector = reflector
        self.plug_board = PlugBoard()
        return

    def set_rotor_settings(self, settings: List[int]):
        for index, setting in enumerate(settings):
            self.rotors[index].set_setting(setting)

    def set_rotor_positions(self, positions: List[str]):
        for index, position in enumerate(positions):
            self.rotors[index].set_position(position)

    def set_plugboard_mapping(self, mapping: str):
        self.plug_board.add(PlugLead(mapping))

    def set_plugboard_mappings(self, mappings: str):
        for mapping in mappings.split():
            self.set_plugboard_mapping(mapping)

    def encode(self, string: str):
        ret = ''
        for char in string:
            ret += self._encode_char(char)

        print("-------")

        return ret

    def _encode_char(self, char: str):
        encoded_char = self.plug_board.encode(char)

        print('ENCODE', encoded_char)

        # rotors LTR
        for index, rotor in enumerate(reversed(self.rotors)):
            actual_index = len(self.rotors) - index - 1
            print("Rotor", index, "char", encoded_char)

            if index == 0:
                self._rotate_rotor(actual_index)

            encoded_char = rotor.encode_right_to_left(encoded_char)

        print("Reflector", encoded_char)

        encoded_char = self.reflector.encode_right_to_left(encoded_char)

        print("Reflected", encoded_char)

        # rotors RTL
        for index, rotor in enumerate(self.rotors):
            print("Rotor", index, "char", encoded_char)
            encoded_char = rotor.encode_left_to_right(encoded_char)

        print("Encoded", encoded_char)
        print("PlugBoard", self.plug_board.encode(encoded_char))

        return self.plug_board.encode(encoded_char)

    def _rotate_rotor(self, index: int):
        print('rotate rotor', index)
        if index < 0 or index >= len(self.rotors):
            return

        if self.rotors[index].should_rotate_next():
            self._rotate_rotor(index - 1)

        self.rotors[index].rotate()
