import unittest

from enigma import PlugLead

class PlugLeadTest(unittest.TestCase):
    def test_plug_lead(self):
        lead = PlugLead("AG")
        
        self.assertEqual(lead.encode("A"), "G")
        self.assertEqual(lead.encode("G"), "A")
        self.assertEqual(lead.encode("D"), "D")

if __name__ == '__main__':
    unittest.main()
