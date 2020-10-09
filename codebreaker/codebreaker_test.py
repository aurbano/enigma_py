# flake8: noqa

import unittest

from codebreaker import Codebreaker


class CodebreakerTest(unittest.TestCase):
    def test_codebreaker(self):
        codebreaker = Codebreaker("CODE")
        self.assertTrue(codebreaker is not None)
