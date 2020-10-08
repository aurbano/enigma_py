from typing import List
from .rotor import Rotor
from .plug_board import Plugboard
from .plug_lead import PlugLead


class Machine:
    def __init__(self, rotors: List[Rotor], reflector: Rotor = None):
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

            if is_first_rotor or should_next_rotor_rotate or (not is_last_rotor and rotor.is_on_notch()):
                if not is_first_rotor:
                    print('notch on first')

                should_next_rotor_rotate = rotor.is_on_notch()
                rotor.rotate()

                # this fixes the long sentence test
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
