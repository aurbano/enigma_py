class PlugLead:
    def __init__(self, mapping: str):
        if len(mapping) != 2:
            raise ValueError(
                'PlugLead must be initialised with 2 leads - "XY"'
            )

        self.mapping = mapping

    def can_encode(self, character: str):
        if self.mapping[0] == character or self.mapping[1] == character:
            return True

        return False

    def encode(self, character: str):
        if len(character) > 1:
            raise ValueError('You can only encode single characters')

        if character == self.mapping[0]:
            return self.mapping[1]
        elif character == self.mapping[1]:
            return self.mapping[0]

        return character
