from .plug_lead import PlugLead

class PlugBoard: 
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