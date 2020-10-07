from typing import List
from .rotor import Rotor
from .plug_board import Plugboard
from .plug_lead import PlugLead


class Machine:
    def __init__(self, rotors: List[Rotor], reflector: Rotor):
        self.rotors = rotors
        self.reflector = reflector
        self.plug_board = Plugboard()
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
        string = string.upper()
        for char in string:
            ret += self._encode_char(char)
        return ret

    def print_state(self):
        settings = ''
        positions = ''
        for rotor in self.rotors:
            positions += rotor.current_position() + ' '
            settings += chr(rotor.setting + ord("A") + 1) + ' '

        print(settings, positions)

    def _encode_char(self, char: str):
        if char < "A" or char > "Z":
            return char

        encoded_char = self.plug_board.encode(char)

        self._rotate_rotors()

        # rotors LTR
        for rotor in reversed(self.rotors):
            encoded_char = rotor.encode_right_to_left(encoded_char)

        # reflector
        encoded_char = self.reflector.encode_right_to_left(encoded_char)

        # rotors RTL
        for rotor in self.rotors:
            encoded_char = rotor.encode_left_to_right(encoded_char)

        return self.plug_board.encode(encoded_char)

    def _rotate_rotors(self):
        # Rotor 0 always turns
        # Rotor 1 turns if rotor 0 is on its notch or if rotor 1 is on its notch
        # Rotor 2 turns if rotor 1 is on its notch
        should_next_rotor_rotate = False
        for index, rotor in enumerate(reversed(self.rotors)):
            if index == 0 or should_next_rotor_rotate or rotor.is_on_notch():
                should_next_rotor_rotate = rotor.is_on_notch()
                rotor.rotate()
            else:
                should_next_rotor_rotate = rotor.is_on_notch()
