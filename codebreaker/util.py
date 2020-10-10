import string
from itertools import product, combinations
from typing import List

def get_combinations_of(items, number):
    return list(product(items, repeat=number))


def generate_all_positions(rotor_count: int):
    alphabet = list(string.ascii_uppercase)
    return list(product(
        alphabet,
        alphabet,
        alphabet
    ))


def swap_rotor_chars(alphabet: str, rotor_pattern: str):
    patterns = []

    # get all unique groups of 4 letters in the alphabet
    letter_groups = list(combinations(list(alphabet), 4))
    for group in letter_groups:
        pattern = swap_letter(alphabet, rotor_pattern, group[0], group[1])
        pattern = swap_letter(alphabet, pattern, group[2], group[3])

        patterns.append(pattern)

    return patterns

def swap_letter(alphabet: str, rotor_pattern: str, char1: str, char2: str):
    pattern = list(rotor_pattern)

    char1_index = rotor_pattern.index(char1)
    char2_index = rotor_pattern.index(char2)

    char1_contact = alphabet[char1_index]
    char2_contact = alphabet[char2_index]

    char1_contact_index = rotor_pattern.index(char1_contact)
    char2_contact_index = rotor_pattern.index(char2_contact)

    swap_list_items(pattern, char1_index, char2_index)
    swap_list_items(pattern, char1_contact_index, char2_contact_index)

    return ''.join(pattern)

def swap_list_items(items: List, idx1: int, idx2: int):
    items[idx1], items[idx2] = items[idx2], items[idx1]