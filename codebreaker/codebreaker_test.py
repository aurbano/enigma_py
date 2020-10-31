# flake8: noqa

from enigma.builtin_rotors import Rotors
from enigma.rotor import Rotor
import unittest
import itertools
import string

from codebreaker import Codebreaker
from .util import generate_all_positions, get_combinations_of, swap_rotor_chars


class CodebreakerTest(unittest.TestCase):
    def test_simple_code(self):
        codebreaker = Codebreaker(
            "UPLDGCVNQ"
        )

        codebreaker.add_known_word('ALEJ')

        codebreaker.add_possible_rotors(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()]
        )

        codebreaker.add_possible_settings([1, 2, 3])
        codebreaker.add_possible_settings([1, 1, 1])

        codebreaker.add_possible_positions(["A", "A", "A"])
        codebreaker.add_possible_positions(["A", "B", "C"])
        codebreaker.add_possible_positions(["A", "A", "Z"])

        codebreaker.add_possible_reflector(Rotors["A"]())
        codebreaker.add_possible_reflector(Rotors["B"]())
        codebreaker.add_possible_reflector(Rotors["C"]())

        decoded = codebreaker.decode(True)

        self.assertEquals(decoded['msg'], 'ALEJANDRO')
        self.assertEquals(decoded['rotors'], ["I", "II", "III"])
        self.assertEquals(decoded['settings'], [1, 1, 1])
        self.assertEquals(decoded['positions'], ["A", "A", "Z"])
        self.assertEquals(decoded['reflector'], "B")
        self.assertEquals(decoded['plugboard'], "")

    def test_code_1(self):
        codebreaker = Codebreaker(
            "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
        )
        codebreaker.add_known_word('SECRETS')

        codebreaker.add_possible_rotors(
            [Rotors["Beta"](), Rotors["Gamma"](), Rotors["V"]()]
        )

        codebreaker.add_possible_reflector(Rotors["A"]())
        codebreaker.add_possible_reflector(Rotors["B"]())
        codebreaker.add_possible_reflector(Rotors["C"]())

        codebreaker.add_possible_settings([4, 2, 14])

        codebreaker.add_possible_positions(["M", "J", "M"])

        codebreaker.add_possible_plugboard("KI XN FL")

        decoded = codebreaker.decode(True)
        self.assertEquals(
            decoded['msg'],
            'NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING'
        )
        self.assertEquals(decoded['rotors'], ["Beta", "Gamma", "V"])
        self.assertEquals(decoded['settings'], [4, 2, 14])
        self.assertEquals(decoded['positions'], ["M", "J", "M"])
        self.assertEquals(decoded['reflector'], "C")
        self.assertEquals(decoded['plugboard'], "KI XN FL")

    def test_code_2(self):
        codebreaker = Codebreaker(
            "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
        )
        codebreaker.add_known_word('UNIVERSITY')

        codebreaker.add_possible_rotors(
            [Rotors["Beta"](), Rotors["I"](), Rotors["III"]()]
        )

        codebreaker.add_possible_reflector(Rotors["B"]())

        codebreaker.add_possible_settings([23, 2, 10])

        for position in generate_all_positions(3):
            codebreaker.add_possible_positions(list(position))

        codebreaker.add_possible_plugboard("VH PT ZG BJ EY FS")

        decoded = codebreaker.decode(True)

        self.assertEquals(
            decoded['msg'],
            'IHOPEYOUAREENJOYINGTHEUNIVERSITYOFBATHEXPERIENCESOFAR'
        )
        self.assertEquals(decoded['rotors'], ["Beta", "I", "III"])
        self.assertEquals(decoded['settings'], [23, 2, 10])
        self.assertEquals(decoded['positions'], ["I", "M", "G"])
        self.assertEquals(decoded['reflector'], "B")
        self.assertEquals(decoded['plugboard'], "VH PT ZG BJ EY FS")

    def test_code_3(self):
        codebreaker = Codebreaker(
            "ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY"
        )
        codebreaker.add_known_word('THOUSANDS')

        possible_rotors = list(itertools.permutations(
            ["II", "Gamma", "IV", "Beta"],
            3
        ))
        for rotors in possible_rotors:
            codebreaker.add_possible_rotors(
                [Rotors[rotor]() for rotor in rotors]
            )

        codebreaker.add_possible_reflector(Rotors["C"]())
        codebreaker.add_possible_reflector(Rotors["B"]())
        codebreaker.add_possible_reflector(Rotors["A"]())

        possible_settings = [
            i for i in range(0, 27)
                if (i % 10) % 2 is 0
                    and int(i / 10) % 2 is 0
        ]

        for settings in get_combinations_of(possible_settings, 3):
            codebreaker.add_possible_settings(list(settings))

        codebreaker.add_possible_positions(["E", "M", "Y"])

        codebreaker.add_possible_plugboard("FH TS BE UQ KD AL")

        decoded = codebreaker.decode(True)

        self.assertEquals(
            decoded['msg'],
            'SQUIRRELSPLANTTHOUSANDSOFNEWTREESEACHYEARBYMERELYFORGETTINGWHERETHEYPUTTHEIRACORNS'
        )
        self.assertEquals(decoded['rotors'], ["II", "Gamma", "IV"])
        self.assertEquals(decoded['settings'], [24, 8, 20])
        self.assertEquals(decoded['positions'], ["E", "M", "Y"])
        self.assertEquals(decoded['reflector'], "C")
        self.assertEquals(decoded['plugboard'], "FH TS BE UQ KD AL")

    def test_code_4(self):
        codebreaker = Codebreaker(
            "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW"
        )
        codebreaker.add_known_word('TUTOR')

        codebreaker.add_possible_rotors(
            [Rotors["V"](), Rotors["III"](), Rotors["IV"]()]
        )

        codebreaker.add_possible_reflector(Rotors["A"]())

        codebreaker.add_possible_settings([24, 12, 10])

        codebreaker.add_possible_positions(["S", "W", "U"])

        # There are some known plugs, and two where we only know one character
        # We know the other character cannot already be in the plugboard
        known_plugs = "WP RJ VF HN CG BS"
        alphabet = list(string.ascii_uppercase)
        existing_plugboard = known_plugs + ' AI'
        remaining_letters = [
            letter for letter in alphabet if letter not in existing_plugboard
        ]
        # The final leads will be combinations of A, I, and the remaining_letters
        combinations_a = list(itertools.product(["A"], remaining_letters))
        combinations_i = list(itertools.product(["I"], remaining_letters))

        combinations = list(filter(
            lambda i: i[0][1] != i[1][1],
            itertools.product(combinations_a, combinations_i)
        ))

        combinations_str = list(map(
            lambda i: i[0][0] + i[0][1] + ' ' + i[1][0] + i[1][1],
            combinations
        ))

        for combination in combinations_str:
            codebreaker.add_possible_plugboard(known_plugs + ' ' + combination)

        decoded = codebreaker.decode()

        self.assertEquals(
            decoded['msg'],
            'NOTUTORSWEREHARMEDNORIMPLICATEDOFCRIMESDURINGTHEMAKINGOFTHESEEXAMPLES'
        )
        self.assertEquals(decoded['rotors'], ["V", "III", "IV"])
        self.assertEquals(decoded['settings'], [24, 12, 10])
        self.assertEquals(decoded['positions'], ["S", "W", "U"])
        self.assertEquals(decoded['reflector'], "A")
        self.assertEquals(decoded['plugboard'], "WP RJ VF HN CG BS AT IK")

    def test_code_5(self):
        codebreaker = Codebreaker(
            "HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX"
        )
        codebreaker.add_known_word('INSTAGRAM')
        codebreaker.add_known_word('FACEBOOK')
        codebreaker.add_known_word('TWITTER')
        codebreaker.add_known_word('YOUTUBE')
        codebreaker.add_known_word('LINKEDIN')
        codebreaker.add_known_word('SNAPCHAT')

        codebreaker.add_possible_rotors(
            [Rotors["V"](), Rotors["II"](), Rotors["IV"]()]
        )

        codebreaker.add_possible_settings([6, 18, 7])
        codebreaker.add_possible_positions(["A", "J", "L"])
        codebreaker.add_possible_plugboard("UG IE PO NX WT")

        # Non standard reflector goes here
        # need to generate variations of rotors A, B, C
        reflector_A = Rotors["A"]().pattern
        reflector_B = Rotors["B"]().pattern
        reflector_C = Rotors["C"]().pattern

        alphabet = string.ascii_uppercase

        variations = {
            "A": swap_rotor_chars(alphabet, reflector_A),
            "B": swap_rotor_chars(alphabet, reflector_B),
            "C": swap_rotor_chars(alphabet, reflector_C),
        }
        reflectors = ["A", "B", "C"]
        decoded = None
        successful_variation = None

        for reflector_name in reflectors:
            for variation in variations[reflector_name]:
                codebreaker.reset_reflector()
                codebreaker.add_possible_reflector(Rotor(reflector_name, variation))

                try:
                    decoded = codebreaker.decode(True)
                    successful_variation = variation
                    break
                except:
                    continue

        if decoded is None:
            raise ValueError("Unable to decode message")

        self.assertEquals(
            decoded['msg'],
            'YOUCANFOLLOWMYDOGONINSTAGRAMATTALESOFHOFFMANN'
        )
        self.assertEquals(decoded['rotors'], ["V", "II", "IV"])
        self.assertEquals(decoded['settings'], [6, 18, 7])
        self.assertEquals(decoded['positions'], ["A", "J", "L"])
        self.assertEquals(decoded['reflector'], "B")
        self.assertEquals(successful_variation, "PQUHRSLDYXNGOKMABEFZCWVJIT")
        self.assertEquals(decoded['plugboard'], "UG IE PO NX WT")
