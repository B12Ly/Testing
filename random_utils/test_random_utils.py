from random_utils.random_utils import guess_int, guess_float
import unittest
from unittest.mock import patch

class TestRandomUtils(unittest.TestCase):
    def test_guess_int_range(self):
        start = 10
        stop = 50
        result = guess_int(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, stop)
        self.assertIsInstance(result, int)

    def test_guess_float_range(self):
        start = 0.5
        stop = 3.5
        result = guess_float(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLess(result, stop)
        self.assertIsInstance(result, float)

    @patch("random.randint")
    def test_guess_int_with_mock(self, mock_randint):
        mock_randint.return_value = 8
        self.assertEqual(guess_int(1, 10), 8)

    @patch("random.uniform")
    def test_guess_float_with_mock(self, mock_uniform):
        mock_uniform.return_value = 2.7
        self.assertEqual(guess_float(0.5, 3.0), 2.7)

    def test_guess_int_with_large_range(self):
        start = 1000
        stop = 10000
        result = guess_int(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, stop)
        self.assertIsInstance(result, int)

    def test_guess_float_with_small_range(self):
        start = 1.1
        stop = 1.5
        result = guess_float(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLess(result, stop)
        self.assertIsInstance(result, float)
