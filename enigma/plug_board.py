from .plug_lead import PlugLead


class Plugboard:
    """Plugboard
    Creates a new plug board for an Enigma machine
    """

    def __init__(self):
        self.leads = []
        return

    def add(self, lead: PlugLead):
        """
        Add a new lead
        """
        self.leads.append(lead)

    def encode(self, character: str):
        """
        Encode a character using the plug board. If no plug is setup for this
        character it will return the character itself.
        """
        if len(self.leads) < 1:
            return character

        plug = next(
            (each_plug for each_plug in self.leads
                if each_plug.can_encode(character)
             ),
            self.leads[0]
        )
        return plug.encode(character)
