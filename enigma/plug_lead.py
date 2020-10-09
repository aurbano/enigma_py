class PlugLead:
    """PlugLead
    Creates a new plug lead for an Enigma machine

    :param mapping: Character mapping for this lead, specified as a string
        with two characters
    """

    def __init__(self, mapping: str):
        if len(mapping) != 2:
            raise ValueError(
                'PlugLead must be initialised with 2 leads - "XY"'
            )

        self.mapping = mapping

    def can_encode(self, character: str):
        """
        Return True if the given character can be encoded using this lead
        """
        if self.mapping[0] == character or self.mapping[1] == character:
            return True

        return False

    def encode(self, character: str):
        """
        Encode a character using this lead. If it's not actually setup to
        convert this character it just returns it unchanged
        """
        if len(character) > 1:
            raise ValueError('You can only encode single characters')

        if character == self.mapping[0]:
            return self.mapping[1]
        elif character == self.mapping[1]:
            return self.mapping[0]

        return character
