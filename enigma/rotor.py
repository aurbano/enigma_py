class Rotor:
    """Create an Enigma Machine Rotor

    :param pattern: The rotor pattern specified as a case-sensitive string (the 
        standard alphabet is uppercase, so unless you specify a custom alphabet
        pass the pattern as uppercase too)
    :param notches: Notches for this rotor, specified as a string
        (if there are multiple characters in the string, the rotor will have
        multiple notches)
        None or an empty string can also be passed if this rotor shouldn't
        have a notch.
    :param alphabet: Input alphabet for this rotor. For standard enigma
        machine rotors this is simply the
        roman alphabet, however custom rotors can be easily created supporting
        additional characters.
    """

    def __init__(
        self,
        name: str,
        pattern: str,
        notches: str = None,
        alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ):
        self.name = name
        self.alphabet = alphabet
        self.max_char_index = len(self.alphabet) - 1

        self.pattern = pattern
        self.position = 0
        self.setting = 0
        self.notches = None

        if notches is not None:
            self.notches = [self._char_to_index(each_notch) for each_notch in list(notches)]

    def set_position(self, position: str):
        """
        Set initial position for this rotor

        :param position: Initial position for the rotor, as a character
        """
        self.position = self._ranged(
            0, self.max_char_index, self._char_to_index(position)
        )

    def get_position(self):
        """
        Get the current position for this rotor
        """
        return self._index_to_char(self.position)

    def set_setting(self, setting: int):
        """
        Set initial setting for this rotor

        :param setting: Initial setting for the rotor, as an integer
        """
        self.setting = self._ranged(0, self.max_char_index, setting - 1)

    def get_setting(self):
        """
        Get initial setting for this rotor
        """
        return self._index_to_char(self.setting)

    def encode_right_to_left(self, char: str):
        """
        Encode a character right-to-left through this rotor.

        :param char: Character to be encoded
        """
        if not self._is_char_in_alphabet(char):
            return char

        in_contact_index = self._get_contact_in(char)
        pin_index = self._char_to_index(self.pattern[in_contact_index])
        return self._get_contact_out(pin_index)

    def encode_left_to_right(self, char: str):
        """
        Encode a character left-to-right through this rotor.

        :param char: Character to be encoded
        """
        if not self._is_char_in_alphabet(char):
            return char

        in_contact_index = self._get_contact_in(char)
        contact_char = self._index_to_char(in_contact_index)
        pin_index = self.pattern.index(contact_char)
        return self._get_contact_out(pin_index)

    def rotate(self):
        """
        Trigger a rotation of this rotor. It will wrap around if it reaches
        the last position available
        """
        self.position = (self.position + 1) % len(self.pattern)

    def has_notch(self):
        """
        Return True if this rotor has any notches
        """
        return self.notches is not None and len(self.notches) > 0

    def is_on_notch(self):
        """
        Return True if the current position is on a notch
        """
        return self.has_notch() and self.position in self.notches

    def _char_to_index(self, char: str):
        """
        Convert an input character into an index in the rotor's alphabet
        """
        try:
            return self.alphabet.index(char)
        except:
            raise ValueError("Notch not in rotor pattern! " + char)

    def _index_to_char(self, index: int):
        """
        Convert an index in the rotor's alphabet into a character
        """
        return self.alphabet[index]

    def _get_contact_in(self, char: str):
        """
        Adjust an input character based on the current position and rotor's
        setting
        """
        in_contact_index = self._char_to_index(char)
        return (
            in_contact_index + self.position - self.setting
        ) % len(self.pattern)

    def _get_contact_out(self, index: int):
        """
        Get the exit character for a given contact adjusting based on current
        position and rotor's setting
        """
        contact_out_index = (index - self.position +
                            self.setting) % len(self.pattern)
        return self._index_to_char(contact_out_index)

    def _ranged(self, min_value, max_value, value):
        """
        Return a value if it is within a range, or the closest value within
        that range otherwise.

        :param min_value: Starting value
        :param max_value: Ending value
        :param value: Value that needs to be within the range
        """
        return max(min_value, min(max_value, value))
    
    def _is_char_in_alphabet(self, char: str):
        return char in self.alphabet