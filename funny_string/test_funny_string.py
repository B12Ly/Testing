from funny_string.funny_string import funnyString
import unittest


class TestFunnyString(unittest.TestCase):
    def test_give_acxz_should_be_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_give_bcxz_should_not_be_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_give_single_char_should_be_funny(self):
        self.assertEqual(funnyString("a"), "Funny")

    def test_give_ab_should_be_funny(self):
        self.assertEqual(
            funnyString("ab"), "Funny" if abs(ord("a") - ord("b")) == abs(ord("b") - ord("a")) else "Not Funny"
        )