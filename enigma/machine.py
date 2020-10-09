from typing import List
from .rotor import Rotor
from .plug_board import Plugboard
from .plug_lead import PlugLead


class Machine:
    def __init__(self, rotors: List[Rotor], reflector: Rotor = None):
        self.rotors = rotors
        self.reflector = reflector
        self.plug_board = Plugboard()
        self.last_turning_rotor = 3
        return

    def set_rotor_settings(self, *settings: int):
        settings_in_range = min(len(self.rotors), len(settings))
        for i in range(settings_in_range):
            self.rotors[i].set_setting(settings[i])

    def set_rotor_positions(self, *positions: str):
        positions_in_range = min(len(self.rotors), len(positions))
        for i in range(positions_in_range):
            self.rotors[i].set_position(positions[i])

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

    def _encode_char(self, char: str):
        if char < "A" or char > "Z":
            return char

        self._rotate_rotors()

        encoded_char = self.plug_board.encode(char)

        # rotors LTR
        for rotor in reversed(self.rotors):
            encoded_char = rotor.encode_right_to_left(encoded_char)

        # reflector
        if self.reflector != None:
            encoded_char = self.reflector.encode_right_to_left(encoded_char)

        # rotors RTL
        for rotor in self.rotors:
            encoded_char = rotor.encode_left_to_right(encoded_char)

        return self.plug_board.encode(encoded_char)

    def _rotate_rotors(self):
        should_next_rotor_rotate = False
        for index, rotor in enumerate(reversed(self.rotors)):
            is_first_rotor = (index == 0)
            is_last_rotor = (index == len(self.rotors) - 1)

            if is_last_rotor and len(self.rotors) > self.last_turning_rotor:
                break

            if is_first_rotor or should_next_rotor_rotate or (not is_last_rotor and rotor.is_on_notch()):
                should_next_rotor_rotate = rotor.is_on_notch()
                rotor.rotate()

                if not should_next_rotor_rotate and not rotor.has_notch():
                    break
            else:
                break

    def _get_positions(self):
        positions = ''
        for rotor in self.rotors:
            positions += rotor.get_position()
        return positions

    def _get_settings(self):
        settings = ''
        for rotor in self.rotors:
            settings += rotor.get_setting()
        return settings
