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

def likelyhood_text_is_english(text: str):
    """
    Simple function to determine what percentage of a string are the most common trigrams in english.
    It looks for the frequency for several indicatorsL
     - Most typical trigrams in English
     - Bigrams that don't occur in English
     - Consonant chains

    Trigrams from "Lewand, Robert (2000). Cryptological Mathematics. The Mathematical Association of America. p. 37. ISBN 978-0-88385-719-9."
    Bigrams from "Peter Norvig. English Letter Frequency Counts: Mayzner Revisited http://norvig.com/mayzner.html - visited 14 Oct 2020"

    This method returns the degree of confidence that the given text is in English, in the range [0, 1] where 
    1 means that it's extremely likely this text is English.

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
    unusual_bigrams = [
        'JQ',
        'QG',
        'QK',
        'QY',
        'QZ',
        'WQ',
        'WZ',
        'ZZ',
        'TF',
    ]
    max_consonants = 4

    percentage_trigrams = abs(0.1 - substr_evaluator(text, trigrams))
    percentage_bigrams = substr_evaluator(text, unusual_bigrams)

    consonant_chain_penalty = consonant_chain_evaluator(text, max_consonants, 0.1)

    weight_trigrams = 1
    weight_bigrams = 4

    max_value = weight_trigrams + weight_bigrams

    # normalised confidence that the given text is english in the range [0, 1]
    # where 1 is very sure that it's valid english
    confidence = max(0, (
        max_value - max(weight_trigrams * percentage_trigrams, weight_bigrams * percentage_bigrams)
    ) / max_value - consonant_chain_penalty)

    return confidence


def consonant_chain_evaluator(text: str, max_consonants, penalty_per_char):
    consonant_chains = re.split(r"[aeiou]+", text, flags=re.I)
    consecutive_consonants = [
        (len(chain) - max_consonants) * penalty_per_char 
        for chain in consonant_chains
        if len(chain) >= max_consonants
    ]
    return sum(consecutive_consonants)

def substr_evaluator(text: str, substrings: List[str]):
    total = 0
    len_found = 0
    for substring in substrings:
        occurences = len([m.start() for m in re.finditer(substring.upper(), text)])
        if occurences > 0:
            total += occurences
            len_found += len(substring) * occurences
    
    return len_found / len(text)