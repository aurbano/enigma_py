class PlugLead:
    def __init__(self, mapping: str):
        if len(mapping) != 2:
            raise ValueError('PlugLead must be initialised with 2 leads - "XY"')
            
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


class Plugboard: 
    def __init__(self):
        self.leads = []
        return
    
    def add(self, lead: PlugLead):
        self.leads.append(lead)
        
    def encode(self, character: str):
        if len(self.leads) < 1:
            return character
            
        plug = next((each_plug for each_plug in self.leads if each_plug.can_encode(character)), self.leads[0])
        return plug.encode(character)
        


# You will need to write more classes, which can be done here or in separate files, you choose.


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    pass
