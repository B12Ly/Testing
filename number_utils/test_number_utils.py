from number_utils.number_utils import is_prime_list

import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_3_5_7_are_primes(self):
        prime_list = [2, 3, 5, 7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_5_6_are_not_primes(self):
        prime_list = [4, 5, 6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_all_ones(self):
        prime_list = [1, 1, 1]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_7_11_13_are_primes(self):
        prime_list = [7, 11, 13]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_4_5_mixed(self):
        prime_list = [2, 4, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)