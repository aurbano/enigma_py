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
    
    def test_enigma_tirpitz(self):
        machine = Machine(
            [Rotors["I-T"](), Rotors["II-T"](), Rotors["III-T"]()],
            Rotors["UKW-T"](),
            Rotors["ETW-T"](),
        )
        machine.set_rotor_positions("A", "A", "A")
        machine.set_rotor_settings(1, 1, 1)

        self.assertEqual(machine.encode("ALEJANDRO"), "FCYVLRRWP")
    
    def test_enigma_swiss_k(self):
        machine = Machine(
            [Rotors["I-K"](), Rotors["II-K"](), Rotors["III-K"]()],
            Rotors["UKW-K"](),
            Rotors["ETW-K"](),
        )
        machine.set_rotor_positions("A", "A", "A")
        machine.set_rotor_settings(1, 1, 1)

        self.assertEqual(machine.encode("ALEJANDRO"), "YAWZILKXJ")
    
    def test_enigma_norenigma(self):
        machine = Machine(
            [Rotors["I-N"](), Rotors["II-N"](), Rotors["III-N"]()],
            Rotors["UKW-N"](),
            Rotors["ETW-N"](),
        )
        machine.set_rotor_positions("A", "A", "A")
        machine.set_rotor_settings(1, 1, 1)

        self.assertEqual(machine.encode("ALEJANDRO"), "QRTZVTLNN")
    
    def test_enigma_d(self):
        machine = Machine(
            [Rotors["I-D"](), Rotors["II-D"](), Rotors["III-D"]()],
            Rotors["UKW-D"](),
            Rotors["ETW-D"](),
        )
        machine.set_rotor_positions("A", "A", "A")
        machine.set_rotor_settings(1, 1, 1)

        self.assertEqual(machine.encode("ALEJANDRO"), "HVMLOHZYV")
    
    def test_enigma_m3(self):
        machine = Machine(
            [Rotors["VI"](), Rotors["VII"](), Rotors["VIII"]()],
            Rotors["B"]()
        )
        machine.set_rotor_positions("A", "A", "A")
        machine.set_rotor_settings(1, 1, 1)

        self.assertEqual(machine.encode("ALEJANDRO"), "GOJZBQJHT")
    
    def test_enigma_kd(self):
        machine = Machine(
            [Rotors["I-KD"](), Rotors["II-KD"](), Rotors["III-KD"]()],
            Rotors["UKW-KD"](),
            Rotors["ETW-KD"](),
        )
        machine.set_rotor_positions("A", "A", "A")
        machine.set_rotor_settings(1, 1, 1)

        self.assertEqual(machine.encode("ALEJANDRO"), "LUGRHZMLH")


if __name__ == '__main__':
    unittest.main()
