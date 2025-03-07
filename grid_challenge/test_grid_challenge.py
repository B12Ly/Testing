from grid_challenge.grid_challenge import gridChallenge
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_sorted_grid_should_return_yes(self):
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")

    def test_unsorted_columns_should_return_no(self):
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")

    def test_single_row_should_return_yes(self):
        self.assertEqual(gridChallenge(["bac"]), "YES")

    def test_two_rows_sorted_columns_should_return_yes(self):
        self.assertEqual(gridChallenge(["bac", "def"]), "YES")

    def test_unsorted_grid_should_return_no(self):
        self.assertEqual(gridChallenge(["zyx", "wvu", "tsr"]), "NO")

    def test_same_chars_in_columns_should_return_yes(self):
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")

    def test_empty_grid_should_return_yes(self):
        self.assertEqual(gridChallenge([""]), "YES")

    def test_grid_with_multiple_unsorted_columns_should_return_no(self):
        self.assertEqual(gridChallenge(["abc", "bca", "cab"]), "NO")

    def test_grid_with_identical_rows_should_return_yes(self):
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa", "aaa"]), "YES")
