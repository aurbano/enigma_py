import unittest

from enigma import Machine
from enigma.builtin_rotors import Rotors


class RotorTest(unittest.TestCase):
    def test_encoding(self):
        rotor = Rotors["III"]()
        rotor.set_position('A')

        self.assertEqual(rotor.encode_right_to_left("A"), "B")

    def test_rotation(self):
        rotor = Rotors["III"]()
        rotor.set_position('A')

        rotor.rotate()

        self.assertEqual(rotor.current_position(), "B")

    def test_notch_rotation(self):
        rotor = Rotors["III"]()
        rotor.set_position('U')

        rotor.rotate()

        self.assertEqual(rotor.current_position(), "V")
        self.assertTrue(rotor.should_rotate_next())

    def test_notch(self):
        rotor = Rotors["III"]()
        rotor.set_position('V')

        self.assertTrue(rotor.should_rotate_next())


if __name__ == '__main__':
    unittest.main()
