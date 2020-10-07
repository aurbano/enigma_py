class Rotor:
    def __init__(self, config: str, notch: str = None):
        self.initial_position = ord("A")
        self.final_position = ord("Z")
        self.char_range = self.final_position - self.initial_position

        self.config = config
        self.position = 0
        self.setting = 0
        self.notch = None

        if notch != None:
            self.notch = ord(notch) - self.initial_position

    def set_position(self, position: str):
        self.position = ord(position) - self.initial_position

    def set_setting(self, setting: int):
        self.setting = max(0, min(self.char_range, setting - 1))

    def encode_right_to_left(self, char: str):
        current_char = ord(char) - self.initial_position

        if current_char < 0 or current_char > self.char_range:
            return char

        # get index of char in rotor accounting for rotation
        entry_index = self._offset_in(current_char)

        # return encoded char
        output_index = ord(self.config[entry_index]) - self.initial_position

        # return character at label accounting for rotation
        return chr(self._offset_out(output_index) + self.initial_position)

    def encode_left_to_right(self, char: str):
        contact_index = self._offset_in(ord(char) - self.initial_position)
        contact_char = chr(contact_index + self.initial_position)
        entry_index = self.config.index(contact_char)

        return chr(self._offset_out(entry_index) + self.initial_position)

    def rotate(self):
        self.position = (self.position + 1) % (self.char_range + 1)

    def should_rotate_next(self):
        if self.notch == None:
            return False

        return self.position == self.notch

    def current_position(self):
        return chr(self.position + self.initial_position)

    def _offset_in(self, char: int):
        return (char + self.position - self.setting) % (self.char_range + 1)

    def _offset_out(self, char: int):
        return (char - self.position + self.setting) % (self.char_range + 1)
