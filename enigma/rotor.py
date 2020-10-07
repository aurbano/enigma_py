class Rotor:
    def __init__(self, config: str, notch: str = 'A'):
        self.initial_position = ord("A")
        self.final_position = ord("Z")
        self.char_range = self.final_position - self.initial_position

        self.config = config
        self.notch = ord(notch) - self.initial_position
        self.position = 0
        self.setting = 0

    def set_position(self, position: str):
        self.position = ord(position) - self.initial_position
        print('set rotor position', self.position)

    def set_setting(self, setting: int):
        self.setting = max(0, min(self.char_range, setting - 1))

    def encode_right_to_left(self, char: str):
        print('entry char', char)
        print('rotor position', self.position)
        current_char = ord(char) - self.initial_position

        if current_char < 0 or current_char > self.char_range:
            return char

        # get index of char in rotor accounting for rotation
        entry_index = self._offset_in(current_char)

        print('entry adjusted', chr(entry_index + self.initial_position))
        print('table', self.config[entry_index])

        # return encoded char
        output_index = ord(self.config[entry_index]) - self.initial_position

        # return character at label accounting for rotation
        return chr(self._offset_out(output_index) + self.initial_position)

    def encode_left_to_right(self, char: str):
        contact_index = self._offset_in(ord(char) - self.initial_position)
        contact_char = chr(contact_index + self.initial_position)

        print('contact', contact_index, contact_char)

        entry_index = self.config.index(contact_char)

        print("table char", entry_index, chr(
            entry_index + self.initial_position))

        output_char = chr(self._offset_out(
            entry_index) + self.initial_position)

        print('output char', output_char)

        return output_char

    def rotate(self):
        self.position = (self.position + 1) % (self.char_range + 1)
        print('rotated', self.position)

    def should_rotate_next(self):
        return self.position - self.setting == self.notch

    def current_position(self):
        return chr(self.position + self.initial_position)

    def _offset_in(self, char: int):
        print('offset_in', char, self.position, self.setting)
        return (char + self.position - self.setting) % (self.char_range + 1)

    def _offset_out(self, char: int):
        return (char - self.position + self.setting) % (self.char_range + 1)
