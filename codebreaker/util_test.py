# flake8: noqa
import unittest, string
from .util import swap_letter, is_english


class UtilTest(unittest.TestCase):
    def test_char_swap(self):
        alphabet = string.ascii_uppercase
        pattern = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        swapped = 'JEMZBLYXVAWFCRQUONTSPIKHGD'

        self.assertEquals(swap_letter(alphabet, pattern, 'E', 'J'), swapped)
    
    def test_is_english(self):
        not_english = [
            'DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ',
            'ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY'
        ]
        english = [
            'NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING',
            'SQUIRRELSPLANTTHOUSANDSOFNEWTREESEACHYEARBYMERELYFORGETTINGWHERETHEYPUTTHEIRACORNS'
        ]

        for text in not_english:
            self.assertFalse(is_english(text))
        
        for text in english:
            self.assertTrue(is_english(text))