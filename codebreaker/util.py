import string
from itertools import product, combinations


def get_combinations_of(items, number):
    return list(product(items, repeat=number))


def generate_all_positions(rotor_count: int):
    alphabet = list(string.ascii_uppercase)
    return list(product(
        alphabet,
        alphabet,
        alphabet
    ))


def rotor_variations(rotor_pattern: str, modify_char_count: int):
    variations = []
    for i1, i2, i3, i4 in combinations(range(len(rotor_pattern)), modify_char_count):
        all_chars = list(rotor_pattern)
        # swap two characters
        all_chars[i1], all_chars[i2] = all_chars[i2], all_chars[i1]
        all_chars[i3], all_chars[i4] = all_chars[i4], all_chars[i3]
        variations.append(''.join(all_chars))

    return variations
