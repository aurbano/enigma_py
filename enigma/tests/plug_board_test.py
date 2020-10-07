import unittest

from enigma import PlugBoard, PlugLead

class PlugBoardTest(unittest.TestCase):
    def test_plug_board(self):
        plugboard = PlugBoard()

        plugboard.add(PlugLead("SZ"))
        plugboard.add(PlugLead("GT"))
        plugboard.add(PlugLead("DV"))
        plugboard.add(PlugLead("KU"))

        self.assertEqual(plugboard.encode("K"), "U")
        self.assertEqual(plugboard.encode("A"), "A")

if __name__ == '__main__':
    unittest.main()