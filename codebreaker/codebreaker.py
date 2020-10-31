import itertools
from typing import List
from enigma.rotor import Rotor
from enigma.machine import Machine
from .util import likelyhood_text_is_english


class Codebreaker:
    def __init__(self, code: str):
        self.code = code
        self.machine = None

        self.known_words_in_output = []

        self.possible_rotors = []
        self.possible_reflectors = []
        self.possible_settings = []
        self.possible_positions = []
        self.possible_plugboards = []
    
    def reset_rotors(self):
        self.possible_rotors = []
    
    def reset_reflector(self):
        self.possible_reflectors = []

    def add_known_word(self, known_word: str):
        self.known_words_in_output.append(known_word)

    def add_possible_rotors(self, rotor: Rotor):
        self.possible_rotors.append(rotor)

    def add_possible_reflector(self, reflector: Rotor):
        self.possible_reflectors.append(reflector)

    def add_possible_settings(self, settings: List[int]):
        self.possible_settings.append(settings)

    def add_possible_positions(self, positions: List[str]):
        self.possible_positions.append(positions)

    def add_possible_plugboard(self, plugboard: str):
        self.possible_plugboards.append(plugboard)

    def decode(self, break_on_crib: bool = False):
        if len(self.possible_plugboards) < 1:
            self.possible_plugboards.append('')

        # Generate all possible combinations of the items to test
        combinations = list(itertools.product(
            self.possible_rotors,
            self.possible_reflectors,
            self.possible_settings,
            self.possible_positions,
            self.possible_plugboards,
        ))

        decoded_str = ''
        valid_combination = None
        max_score = 0

        for index, combination in enumerate(combinations):
            rotors = combination[0]
            reflector = combination[1]
            settings = combination[2]
            positions = combination[3]
            plugboard = combination[4]

            # Prepare the machine
            machine = Machine(rotors, reflector)

            machine.set_rotor_positions(*positions)
            machine.set_rotor_settings(*settings)

            if len(plugboard) > 0:
                machine.set_plugboard_mappings(plugboard)

            decoded_str = machine.encode(self.code)
            score = self._test_decoding(decoded_str, break_on_crib)

            if score > max_score:
                max_score = score
                valid_combination = index
            
            if score >= 0.9:
                break

        if valid_combination is not None:
            return {
                'msg': decoded_str,
                'rotors': [rotor.name for rotor in combinations[valid_combination][0]],
                'reflector': combinations[valid_combination][1].name,
                'settings': combinations[valid_combination][2],
                'positions': combinations[valid_combination][3],
                'plugboard': combinations[valid_combination][4],
            }

        raise ValueError("Unable to decode message.")

    def _test_decoding(self, decoded_str: str, break_on_crib: bool):
        for crib in self.known_words_in_output:
            if crib not in decoded_str:
                return 0
            if break_on_crib and crib in decoded_str:
                return 1

        return likelyhood_text_is_english(decoded_str)
