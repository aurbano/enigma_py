from .rotor import Rotor

Rotors = {
    # M4 R2
    "Beta": lambda: Rotor("Beta", "LEYJVCNIXWPBQMDRTAKZGFUHOS"),
    "Gamma": lambda: Rotor("Gamma", "FSOKANUERHMBTIYCWLQPZXVGJD"),

    # German Railway (Rocket) 
    "I": lambda: Rotor("I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": lambda: Rotor("II", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": lambda: Rotor("III", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": lambda: Rotor("IV", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": lambda: Rotor("V", "VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),

    "A": lambda: Rotor("A", "EJMZALYXVBWFCRQUONTSPIKHGD"),
    "B": lambda: Rotor("B", "YRUHQSLDPXNGOKMIEBFZCWVJAT"),
    "C": lambda: Rotor("C", "FVPJIAOYEDRZXWGCTKUQSBNMHL"),

    # Enigma I
    "ETW": lambda: Rotor("ETW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),

    # Extension: Add all Enigma rotors

    # Enigma D
    "I-D": lambda: Rotor("I-D", "LPGSZMHAEOQKVXRFYBUTNICJDW", "Y"),
    "II-D": lambda: Rotor("II-D", "SLVGBTFXJQOHEWIRZYAMKPCNDU", "E"),
    "III-D": lambda: Rotor("III-D", "CJGDPSHKTURAWZXFMYNQOBVLIE", "N"),
    "UKW-D": lambda: Rotor("UKW-D", "IMETCGFRAYSQBZXWLHKDVUPOJN"),
    "ETW-D": lambda: Rotor("ETW-D", "QWERTZUIOASDFGHJKPYXCVBNML"),
    
    # Enigma KD
    "I-KD": lambda: Rotor("I-KD", "VEZIOJCXKYDUNTWAPLQGBHSFMR", "SUYAEHLNQ"),
    "II-KD": lambda: Rotor("II-KD", "HGRBSJZETDLVPMQYCXAOKINFUW", "SUYAEHLNQ"),
    "III-KD": lambda: Rotor("III-KD", "NWLHXGRBYOJSAZDVTPKFQMEUIC", "SUYAEHLNQ"),
    "UKW-KD": lambda: Rotor("UKW-KD", "KOTVPNLMJIAGHFBEWYXCZDQSRU"),
    "ETW-KD": lambda: Rotor("ETW-KD", "QWERTZUIOASDFGHJKPYXCVBNML"),

    # Railway Enigma
    "I-Railway": lambda: Rotor("I-Railway", "JGDQOXUSCAMIFRVTPNEWKBLZYH", "N"),
    "II-Railway": lambda: Rotor("II-Railway", "NTZPSFBOKMWRCJDIVLAEYUXHGQ", "E"),
    "III-Railway": lambda: Rotor("III-Railway", "JVIUBHTCDYAKEQZPOSGXNRMWFL", "Y"),
    "UKW-Railway": lambda: Rotor("UKW-Railway", "QYHOGNECVPUZTFDJAXWMKISRBL"),
    "ETW-Railway": lambda: Rotor("ETW-Railway", "QWERTZUIOASDFGHJKPYXCVBNML"),

    # M3 & M4 Naval
    "VI": lambda: Rotor("VI", "JPGVOUMFYQBENHZRDKASXLICTW", "ZM"),
    "VII": lambda: Rotor("VII", "NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM"),
    "VIII": lambda: Rotor("VIII", "FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM"),

    # Swiss K
    "I-K": lambda: Rotor("I-K", "PEZUOHXSCVFMTBGLRINQJWAYDK", "Y"),
    "II-K": lambda: Rotor("II-K", "ZOUESYDKFWPCIQXHMVBLGNJRAT", "E"),
    "III-K": lambda: Rotor("III-K", "EHRVXGAOBQUSIMZFLYNWKTPDJC", "N"),
    "UKW-K": lambda: Rotor("UKW-K", "IMETCGFRAYSQBZXWLHKDVUPOJN"),
    "ETW-K": lambda: Rotor("ETW-K", "QWERTZUIOASDFGHJKPYXCVBNML"),

    # Norway (Norenigma)
    "I-N": lambda: Rotor("I-N", "WTOKASUYVRBXJHQCPZEFMDINLG", "Q"),
    "II-N": lambda: Rotor("II-N", "GJLPUBSWEMCTQVHXAOFZDRKYNI", "E"),
    "III-N": lambda: Rotor("III-N", "JWFMHNBPUSDYTIXVZGRQLAOEKC", "V"),
    "IV-N": lambda: Rotor("IV-N", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V-N": lambda: Rotor("V-N", "HEJXQOTZBVFDASCILWPGYNMURK", "Z"),
    "UKW-N": lambda: Rotor("UKW-N", "MOWJYPUXNDSRAIBFVLKZGQCHET"),
    "ETW-N": lambda: Rotor("ETW-N", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),

    # M4 R1 (M3 + Thin)
    "B-thin": lambda: Rotor("B-thin", "ENKQAUYWJICOPBLMDXZVFTHRGS"),
    "C-thin": lambda: Rotor("C-thin", "RDOBJNTKVEHMLFCWZAXGYIPSUQ"),

    # Enigma T - Tirpitz (Japanese Variant)
    "I-T": lambda: Rotor("I-T", "KPTYUELOCVGRFQDANJMBSWHZXI", "WZEKQ"),
    "II-T": lambda: Rotor("II-T", "UPHZLWEQMTDJXCAKSOIGVBYFNR", "WZFLR"),
    "III-T": lambda: Rotor("III-T", "QUDLYRFEKONVZAXWHMGPJBSICT", "WZEKQ"),
    "IV-T": lambda: Rotor("IV-T", "CIWTBKXNRESPFLYDAGVHQUOJZM", "WZFLR"),
    "V-T": lambda: Rotor("V-T", "UAXGISNJBVERDYLFZWTPCKOHMQ", "YCFKR"),
    "VI-T": lambda: Rotor("VI-T", "XFUZGALVHCNYSEWQTDMRBKPIOJ", "XEIMQ"),
    "VII-T": lambda: Rotor("VII-T", "BJVFTXPLNAYOZIKWGDQERUCHSM", "YCFKR"),
    "VIII-T": lambda: Rotor("VIII-T", "YMTPNZHWKODAJXELUQVGCBISFR", "XEIMQ"),
    "UKW-T": lambda: Rotor("UKW-T", "GEKPBTAUMOCNILJDXZYFHWVQSR"),
    "ETW-T": lambda: Rotor("ETW-T", "KZROUQHYAIGBLWVSTDXFPNMCJE"),
}