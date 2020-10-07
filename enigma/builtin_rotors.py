from enum import Enum

from .rotor import Rotor

RotorName = Enum('RotorName', 'Beta Gamma I II III IV V A B C')

# TODO this is not immutable!
Rotors = {
    "Beta": lambda: Rotor("LEYJVCNIXWPBQMDRTAKZGFUHOS"),
    "Gamma": lambda: Rotor("FSOKANUERHMBTIYCWLQPZXVGJD"),

    "I": lambda: Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": lambda: Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": lambda: Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": lambda: Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": lambda: Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),

    "A": lambda: Rotor("EJMZALYXVBWFCRQUONTSPIKHGD"),
    "B": lambda: Rotor("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "C": lambda: Rotor("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
}
