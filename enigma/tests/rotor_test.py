# flake8: noqa
import unittest

from enigma.builtin_rotors import Rotors


class RotorTest(unittest.TestCase):
    def test_encoding(self):
        rotor = Rotors["III"]()
        rotor.set_position('A')

        self.assertEqual(rotor.encode_right_to_left("A"), "B")

    def test_setting_position(self):
        rotor = Rotors["III"]()
        rotor.set_setting(2)
        rotor.set_position('A')

        rotor.rotate()
        self.assertEqual(rotor.get_position(), "B")
        self.assertEqual(rotor.encode_right_to_left("A"), "B")
        rotor.rotate()
        self.assertEqual(rotor.get_position(), "C")
        self.assertEqual(rotor.encode_right_to_left("A"), "C")
        rotor.rotate()
        self.assertEqual(rotor.get_position(), "D")
        self.assertEqual(rotor.encode_right_to_left("A"), "D")
        rotor.rotate()
        self.assertEqual(rotor.get_position(), "E")
        self.assertEqual(rotor.encode_right_to_left("A"), "E")

    def test_setting_position_2(self):
        rotor = Rotors["II"]()
        rotor.set_setting(26)
        rotor.set_position('Z')

        rotor.rotate()
        self.assertEqual(rotor.get_position(), "A")
        self.assertEqual(rotor.encode_right_to_left("A"), "I")
        rotor.rotate()
        self.assertEqual(rotor.get_position(), "B")
        self.assertEqual(rotor.encode_right_to_left("A"), "B")
        rotor.rotate()
        self.assertEqual(rotor.get_position(), "C")
        self.assertEqual(rotor.encode_right_to_left("A"), "H")
        rotor.rotate()
        self.assertEqual(rotor.get_position(), "D")
        self.assertEqual(rotor.encode_right_to_left("A"), "O")

    def test_rotation(self):
        rotor = Rotors["III"]()
        rotor.set_position('A')

        rotor.rotate()

        self.assertEqual(rotor.get_position(), "B")

    def test_rotation_wrapping(self):
        rotor = Rotors["I"]()
        rotor.set_position('Z')

        rotor.rotate()

        self.assertEqual(rotor.get_position(), "A")

    def test_notch(self):
        rotor = Rotors["III"]()
        rotor.set_position('V')

        self.assertTrue(rotor.is_on_notch())

    def test_notch_rotation(self):
        rotor = Rotors["III"]()
        rotor.set_position('U')

        rotor.rotate()

        self.assertEqual(rotor.get_position(), "V")
        self.assertTrue(rotor.is_on_notch())


if __name__ == '__main__':
    unittest.main()
