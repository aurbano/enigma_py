import unittest

from enigma import Machine
from enigma.builtin_rotors import Rotors


class MachineTest(unittest.TestCase):
    def test_encoding_char_1(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            [1, 1, 1]
        )
        machine.set_rotor_positions(
            ["A", "A", "Z"]
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "UPLDGCVNQ")

    def test_encoding_char_2(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            [1, 1, 1]
        )
        machine.set_rotor_positions(
            ["A", "A", "A"]
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "BECZOEFTM")

    def test_encoding_char_3(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            [1, 1, 1]
        )
        machine.set_rotor_positions(
            ["Q", "E", "V"]
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "LVNAGPPQY")

    def test_encoding_char_4(self):
        machine = Machine(
            [Rotors["IV"](), Rotors["V"](), Rotors["Beta"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            [14, 9, 24]
        )
        machine.set_rotor_positions(
            ["A", "A", "A"]
        )

        self.assertEqual(machine.encode("H"), "Y")

    def test_encoding_char_5(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"](), Rotors["IV"]()],
            Rotors["C"]()
        )
        machine.set_rotor_settings(
            [7, 11, 15, 19]
        )
        machine.set_rotor_positions(
            ["Q", "E", "V", "Z"]
        )

        self.assertEqual(machine.encode("Z"), "V")

    def test_encoding_char_6(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            [7, 11, 15]
        )
        machine.set_rotor_positions(
            ["Q", "E", "V"]
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "IBVFUMNND")

    def test_encoding_sentence_1(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(
            [1, 1, 1]
        )
        machine.set_rotor_positions(
            ["A", "A", "Z"]
        )
        machine.set_plugboard_mappings("HL MO AJ CX BZ SR NI YW DG PK")

        self.assertEqual(machine.encode("HELLOWORLD"), "RFKTMBXVVW")

    def test_encoding_sentence_2(self):
        machine = Machine(
            [Rotors["IV"](), Rotors["V"](), Rotors["Beta"](), Rotors["I"]()],
            Rotors["A"]()
        )

        machine.set_rotor_settings(
            [18, 24, 3, 5]
        )
        machine.set_rotor_positions(
            ["E", "Z", "G", "P"]
        )
        machine.set_plugboard_mappings("PC XZ FM QA ST NB HY OR EV IU")

        self.assertEqual(machine.encode("BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI"),
                         "CONGRATULATIONSONPRODUCINGYOURWORKINGENIGMAMACHINESIMULATOR")


if __name__ == '__main__':
    unittest.main()
