class Rotor:
    def __init__(self, pattern: str, notch: str = None):
        self.initial_position = ord("A")
        self.final_position = ord("Z")
        self.char_range = self.final_position - self.initial_position

        self.pattern = pattern
        self.position = 0
        self.setting = 0
        self.notch = None

        if notch != None:
            self.notch = ord(notch) - self.initial_position

    def set_position(self, position: str):
        self.position = self._ranged(
            0, self.char_range, ord(position) - self.initial_position
        )

    def set_setting(self, setting: int):
        self.setting = self._ranged(0, self.char_range, setting - 1)

    def encode_right_to_left(self, char: str):
        in_contact_index = self._get_contact_in(char)
        pin_index = ord(self.pattern[in_contact_index]) - self.initial_position
        return self._get_pin_out(pin_index)

    def encode_left_to_right(self, char: str):
        in_contact_index = self._get_contact_in(char)
        contact_char = chr(in_contact_index + self.initial_position)
        pin_index = self.pattern.index(contact_char)
        return self._get_pin_out(pin_index)

    def rotate(self):
        self.position = (self.position + 1) % (self.char_range + 1)

    def is_on_notch(self):
        if self.notch == None:
            return False

        return self.position == self.notch

    def current_position(self):
        return chr(self.position + self.initial_position)

    def _get_contact_in(self, char: str):
        in_contact_index = ord(char) - self.initial_position
        return self._offset_in(in_contact_index)

    def _get_pin_out(self, index: int):
        return chr(self._offset_out(index) + self.initial_position)

    def _offset_in(self, char: int):
        return (char + self.position - self.setting) % (self.char_range + 1)

    def _offset_out(self, char: int):
        return (char - self.position + self.setting) % (self.char_range + 1)

    def _ranged(self, min_value, max_value, value):
        return max(min_value, min(max_value, value))
