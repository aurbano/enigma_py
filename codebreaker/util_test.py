# flake8: noqa
import unittest, string
from .util import swap_letter, likelyhood_text_is_english


class UtilTest(unittest.TestCase):
    def test_char_swap(self):
        alphabet = string.ascii_uppercase
        pattern = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        swapped = 'JEMZBLYXVAWFCRQUONTSPIKHGD'

        self.assertEquals(swap_letter(alphabet, pattern, 'E', 'J'), swapped)
    
    def test_likelihood_english_each_code(self):
        codes = [
            {
                'valid': 'YOUCANFOLLOWMYDOGONINSTAGRAMATTALESOFHOFFMANN',
                'invalid': [
                    'YOUCGRFOYLONMYIOGHDINCEPGKTIATFBLEBOFHGUFMENN',
                    'HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX',
                    'RNKMANUKLSEUSBJJPSSMMEHNPDLTMUYOMRIQUOOEHVAJL',
                    'WJKMUYUKISZTABSJPESMMEYIPLRZATXHMEAQUONMHVHJL',
                    'YOUCQBFOTLOTMHUOGENIOSYXGCAZATXELETOMHAFFMWUN',
                    'YOUCQRFOYLONMZIOLHNIHSEPGKAIATFBLEBOFHGFEMWNN',
                ]
            },
            {
                'valid': 'NICEWORKYOUVEMANAGEDTODECODETHEFIRSTSECRETSTRING',
                'invalid': [
                    'DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ'
                ]
            },
            {
                'valid': 'IHOPEYOUAREENJOYINGTHEUNIVERSITYOFBATHEXPERIENCESOFAR',
                'invalid': [
                    'CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH',
                    'VEQMEUNEGCZXUMVAZSKSUTJJZBZKQPRKVESMLLETVHUCIODWBUIZG',
                    'ZEBPYHGSNUULEBVOYLDCEQOYZYFEKOFOJQRZIABYCODUGUDYOPZZR',
                    'NKMKOJFQYAXFWXACEFGDAKPDBEVXWECMWEDOUNBORZZUURHBEOFYR',
                ]
            },
            {
                'valid': 'SQUIRRELSPLANTTHOUSANDSOFNEWTREESEACHYEARBYMERELYFORGETTINGWHERETHEYPUTTHEIRACORNS',
                'invalid': [
                    'ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY',
                    'SIJBZUNWZIBVQHWTVQAMGBFEWULANKUIGVEXIGSRSIDURBOOAHLBANPHQXLTCLQEOQNRQXMGVSMESRCICG'
                ]
            },
            {
                'valid': 'NOTUTORSWEREHARMEDNORIMPLICATEDOFCRIMESDURINGTHEMAKINGOFTHESEEXAMPLES',
                'invalid': [
                    'NHTUTORSWEREHARMEIEORKZSLKCATEIOFCRKMESIURKNGTHEZADKNGOFTHXSEEXAMPLES',
                    'SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW',
                    'NYDLDBRSWEREKTRMFANORKSULICTDEAOFCRIMESAURINGEHECTKINGOFDHESEEXDMPLES',
                    'NOEIEBRSWARALARMFDAORVMPIKCTEADOFCRKMASDURKEGDHAMTLKNGOFEOCSAAXEMPIAS'
                ]
            },
        ]

        for code in codes:
            valid_score = likelyhood_text_is_english(code['valid'])
            for invalid in code['invalid']:
                invalid_score = likelyhood_text_is_english(invalid)
                print(code['valid'], invalid, invalid_score, valid_score)
                self.assertLess(invalid_score, valid_score)
