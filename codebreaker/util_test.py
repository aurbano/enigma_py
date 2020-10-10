# flake8: noqa
import unittest, string
from .util import swap_letter


class UtilTest(unittest.TestCase):
    def test_char_swap(self):
        alphabet = string.ascii_uppercase
        #          ABCDEFGHIJKLMNOPQRSTUVWXYZ
        pattern = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        #          _-CD_FGHI-KLMNOPQRSTUVWXYZ
        swapped = 'JEMZBLYXVAWFCRQUONTSPIKHGD'

        self.assertEquals(swap_letter(alphabet, pattern, 'E', 'J'), swapped)