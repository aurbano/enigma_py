import unittest

from enigma import *

class EnigmaTest(unittest.TestCase):
    def test_plug_lead(self):
        lead = PlugLead("AG")
        
        self.assertEqual(lead.encode("A"), "G")
        self.assertEqual(lead.encode("G"), "A")
        self.assertEqual(lead.encode("D"), "D")
    
    def test_plug_board(self):
        plugboard = Plugboard()

        plugboard.add(PlugLead("SZ"))
        plugboard.add(PlugLead("GT"))
        plugboard.add(PlugLead("DV"))
        plugboard.add(PlugLead("KU"))

        self.assertEqual(plugboard.encode("K"), "U")
        self.assertEqual(plugboard.encode("A"), "A")

if __name__ == '__main__':
    unittest.main()
