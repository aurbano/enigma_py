from .rotor import Rotor

Rotors = {
    "Beta": lambda: Rotor("Beta", "LEYJVCNIXWPBQMDRTAKZGFUHOS"),
    "Gamma": lambda: Rotor("Gamma", "FSOKANUERHMBTIYCWLQPZXVGJD"),

    "I": lambda: Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": lambda: Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": lambda: Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": lambda: Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": lambda: Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),

    "A": lambda: Rotor("A", "EJMZALYXVBWFCRQUONTSPIKHGD"),
    "B": lambda: Rotor("B", "YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "C": lambda: Rotor("C", "FVPJIAOYEDRZXWGCTKUQSBNMHL"),

    "B-thin": lambda: Rotor("B-thin", "ENKQAUYWJICOPBLMDXZVFTHRGS"),
    "C-thin": lambda: Rotor("C-thin", "RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
}