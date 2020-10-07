import unittest

from enigma import Machine


class MachineTest(unittest.TestCase):
    def test_machine_encoding(self):
        machine = Machine()

        self.assertEqual(machine.encode("SOMETHING"), "SOMETHING")


if __name__ == '__main__':
    unittest.main()
