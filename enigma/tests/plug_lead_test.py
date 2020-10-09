# flake8: noqa
import unittest

from enigma import PlugLead


class PlugLeadTest(unittest.TestCase):
    def test_plug_lead(self):
        lead = PlugLead("AG")

        self.assertEqual(lead.encode("A"), "G")
        self.assertEqual(lead.encode("G"), "A")
        self.assertEqual(lead.encode("D"), "D")
        self.assertEqual(lead.encode("Z"), "Z")

    def test_invalid_constructor(self):
        with self.assertRaises(ValueError):
            PlugLead("A")

    def test_invalid_encoding(self):
        with self.assertRaises(ValueError):
            lead = PlugLead("AB")
            lead.encode("str")


if __name__ == '__main__':
    unittest.main()
