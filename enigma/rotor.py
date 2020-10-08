class Rotor:
    def __init__(self, pattern: str, notch: str = None):
        self.initial_position = ord("A")
        self.final_position = ord("Z")
        self.max_char_index = self.final_position - self.initial_position

        self.pattern = pattern
        self.position = 0
        self.setting = 0
        self.notch = None

        if notch != None:
            self.notch = self._char_to_index(notch)

    def set_position(self, position: str):
        self.position = self._ranged(
            0, self.max_char_index, self._char_to_index(position)
        )

    def get_position(self):
        return self._index_to_char(self.position)

    def set_setting(self, setting: int):
        self.setting = self._ranged(0, self.max_char_index, setting - 1)

    def get_setting(self):
        return self._index_to_char(self.setting)

    def encode_right_to_left(self, char: str):
        in_contact_index = self._get_contact_in(char)
        pin_index = self._char_to_index(self.pattern[in_contact_index])
        return self._get_pin_out(pin_index)

    def encode_left_to_right(self, char: str):
        in_contact_index = self._get_contact_in(char)
        contact_char = self._index_to_char(in_contact_index)
        pin_index = self.pattern.index(contact_char)
        return self._get_pin_out(pin_index)

    def rotate(self):
        self.position = (self.position + 1) % (self.max_char_index + 1)

    def has_notch(self):
        return self.notch != None

    def is_on_notch(self):
        return self.has_notch() and self.position == self.notch

    def _char_to_index(self, char: str):
        return ord(char) - self.initial_position

    def _index_to_char(self, index: int):
        return chr(index + self.initial_position)

    def _get_contact_in(self, char: str):
        in_contact_index = self._char_to_index(char)
        return self._offset_in(in_contact_index)

    def _get_pin_out(self, index: int):
        return self._index_to_char(self._offset_out(index))

    def _offset_in(self, char: int):
        return (char + self.position - self.setting) % (self.max_char_index + 1)

    def _offset_out(self, char: int):
        return (char - self.position + self.setting) % (self.max_char_index + 1)

    def _ranged(self, min_value, max_value, value):
        return max(min_value, min(max_value, value))
