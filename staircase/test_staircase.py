from staircase.staircase import staircase
import unittest


class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # Arrange
        n = 2
        pattern = "#"
        expected_output = "#\n##"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_3_with_star_should_be_star_starstar_starstarstar(self):
        # Arrange
        n = 3
        pattern = "*"
        expected_output = "*\n**\n***"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_1_with_plus_should_be_plus(self):
        # Arrange
        n = 1
        pattern = "+"
        expected_output = "+"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_0_with_hash_should_be_empty(self):
        # Arrange
        n = 0
        pattern = "#"
        expected_output = ""

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    def test_give_4_with_dollar_should_be_dollar_dollardollar_dollardollardollar_dollardollardollardollar(self):
        # Arrange
        n = 4
        pattern = "$"
        expected_output = "$\n$$\n$$$\n$$$$"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")