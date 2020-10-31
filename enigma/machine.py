from typing import List
from .rotor import Rotor
from .plug_board import Plugboard
from .plug_lead import PlugLead


class Machine:
    """Machine
    Creates a new Enigma machine

    :param rotors: A list of Rotor objects

    :param reflector: A rotor to be used as a reflector. Optional, if not
        specified the machine will simply do a right-to-left encoding and
        then left-to-right directly.
    """

    def __init__(self, rotors: List[Rotor], reflector: Rotor):
        self.rotors = rotors
        self.reflector = reflector
        self.plug_board = Plugboard()
        self.last_turning_rotor = 3
        return

    def set_rotor_settings(self, *settings: int):
        """
        Set initial settings for each rotor

        :param settings: Pass each setting as an argument. They will be
            applied to the rotors in the order supplied (left to right)
            Settings must be passed as integers. Parameters outside the
            alphabet range will be capped.
        """
        settings_in_range = min(len(self.rotors), len(settings))
        for i in range(settings_in_range):
            self.rotors[i].set_setting(settings[i])

    def set_rotor_positions(self, *positions: str):
        """
        Set initial positions for each rotor

        :param positions: Pass each position as an argument. They will be
            applied to the rotors in the order supplied (left to right)
            Positions must be passed as characters. Parameters outside
            the alphabet range will be capped.
        """
        positions_in_range = min(len(self.rotors), len(positions))
        for i in range(positions_in_range):
            self.rotors[i].set_position(positions[i])

    def set_plugboard_mapping(self, mapping: str):
        """
        Add a PlugBoard lead

        :param mapping: Must be two characters in one string
        """
        self.plug_board.add(PlugLead(mapping))

    def set_plugboard_mappings(self, mappings: str):
        """
        Add several PlugBoard leads

        :param mapping: Must be a string consisting of character pairs
            separated by spaces. i.e. "AB CD EF"
        """
        for mapping in mappings.split():
            self.set_plugboard_mapping(mapping)

    def encode(self, string: str):
        """
        Encode a string using the Enigma machine

        :param string: String to be encoded. Unknown characters will be
            preserved in the output. This is case-sensitive and standard
            rotors use uppercase letters only.
        """
        ret = ''
        for char in string:
            ret += self._encode_single_char(char)
        return ret

    def _encode_single_char(self, char: str):
        """
        Encode a single character using the Enigma machine

        :param char: Character to be encoded. This is case-sensitive and
            standard rotors use uppercase letters only.
        """
        if len(char) > 1:
            raise ValueError("_encode_single_char must be called with one character at a time")

        if not self._is_in_alphabet(char):
            return char

        self._rotate_rotors()

        encoded_char = self.plug_board.encode(char)

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
        """
        Trigger a rotation of the rotors, starting by turning the right-most
        rotor. This should be called once for every keypress, before encoding.
        """
        should_next_rotor_rotate = False
        for index, rotor in enumerate(reversed(self.rotors)):
            is_first_rotor = (index == 0)
            is_last_rotor = (index == len(self.rotors) - 1)

            if is_last_rotor and len(self.rotors) > self.last_turning_rotor:
                break

            if is_first_rotor or should_next_rotor_rotate or (
                not is_last_rotor and rotor.is_on_notch()
            ):
                should_next_rotor_rotate = rotor.is_on_notch()
                rotor.rotate()

                if not should_next_rotor_rotate and not rotor.has_notch():
                    break
            else:
                break

    def _get_positions(self):
        """
        Get the current rotor positions as a string.
        """
        positions = ''
        for rotor in self.rotors:
            positions += rotor.get_position()
        return positions

    def _get_settings(self):
        """
        Get the current rotor settings as a string.
        """
        settings = ''
        for rotor in self.rotors:
            settings += rotor.get_setting()
        return settings
    
    def _is_in_alphabet(self, char: str):
        """
        Check if a given char is in any of the rotors' alphabets
        """
        in_alphabet = False
        for rotor in self.rotors:
            in_alphabet = rotor._is_char_in_alphabet(char)
            if in_alphabet:
                break
        
        return in_alphabet