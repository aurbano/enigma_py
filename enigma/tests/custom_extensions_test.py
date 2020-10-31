# flake8: noqa

import unittest

from enigma import Machine, Rotor
from enigma.builtin_rotors import Rotors
from enigma.tests.data.sample import sample_long_input, sample_a


class CustomExtensionsTest(unittest.TestCase):
    def test_machine_encodes_custom_alphabets(self):
        custom_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        rotor = Rotor(
            "Test",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",
            "b",
            custom_alphabet
        )
        reflector = Rotor(
            "Reflector",
            "ejmzalyxvbwfcrquontspikhgdEJMZALYXVBWFCRQUONTSPIKHGD0987654321",
            None,
            custom_alphabet
        )

        machine = Machine(
            [rotor],
            reflector
        )

        machine.set_rotor_positions(custom_alphabet[0])

        initial_str = "Enigma Can Encode Case Sensitively With numbers like 123"
        encoded_str = "ArvYce MeR ARmgpa Wexa 6aHxjwjug9Q Mj3d 8Za6gnt PtWg 50c"

        # encodes string properly
        self.assertEqual(
            machine.encode(initial_str),
            encoded_str
        )

        machine.set_rotor_positions(custom_alphabet[0])

        # decodes string properly
        self.assertEqual(
            encoded_str,
            machine.encode(initial_str)
        )


if __name__ == '__main__':
    unittest.main()
