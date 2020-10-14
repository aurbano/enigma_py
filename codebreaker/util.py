import string, re
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

def is_english(text: str):
    """
    Simple function to determine what percentage of a string are the most common trigrams in english.
    Trigrams taken from "Lewand, Robert (2000). Cryptological Mathematics. The Mathematical Association of America. p. 37. ISBN 978-0-88385-719-9."
    Frequency taken from  "Linton, Tom (2001). "Relative Frequencies of Letters in General English Plain text". Central College. Cryptography (Spring ed.). Archived from the original on January 22, 2007."

    Both sources found under the Wikipedia article on English Trigrams.

    This method will return the percentage with which this trigrams happen, which is a very naive approach but when comparing
    random characters with English concatenated words it produces results that are good enough.

    In order to ensure false positives are less likely to be present in the output the algorithm then checks the longest consecutive
    string made of consonants, as it's unlikely English will have 4-5 at most.

    If the string had been made up of words separated by spaces, other more accurate approaches could've been followed, such as
    dictionary lookup of common words, naive bayes analysis...

    :param text: Original text where the frequency analysis is going to be performed.
    """
    trigrams = [
        'the',
        'and',
        'tha',
        'ent',
        'ing',
        'ion',
        'tio',
        'for',
        'nde',
        'has',
        'nce',
        'edt',
        'tis',
        'oft',
        'sth',
        'men',
    ]
    expected_frequency = 0.15
    max_consonants = 4

    return trigram_evaluator(text, trigrams, expected_frequency, max_consonants)

    
def trigram_evaluator(text: str, trigrams: List[str], expected_frequency: int, max_consecutive_consonants: int):
    total = 0
    len_found = 0
    for trigram in trigrams:
        occurences = len([m.start() for m in re.finditer(trigram.upper(), text)])
        if occurences > 0:
            total += occurences
            len_found += len(trigram) * occurences
    
    found_percentage = len_found / len(text)

    if found_percentage < expected_frequency:
        return False
    
    consecutive_consonants = re.split(r"[aeiou]+", text, flags=re.I)
    longest_consecutive_consonants = len(max(consecutive_consonants, key=len))

    return longest_consecutive_consonants <= max_consecutive_consonants