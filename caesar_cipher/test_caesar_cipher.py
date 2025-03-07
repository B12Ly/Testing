from caesar_cipher.caesar_cipher import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_give_middle_outz_k2_should_return_okffng_qwvb(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_give_XYZ_k3_should_return_ABC(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_give_abc123_k26_should_return_abc123(self):
        self.assertEqual(caesarCipher("abc123!", 26), "abc123!")

    def test_give_z_k1_should_return_a(self):
        self.assertEqual(caesarCipher("z", 1), "a")

    def test_give_empty_string_should_return_empty(self):
        self.assertEqual(caesarCipher("", 5), "")

    def test_give_hello_world_k5_should_return_mjqqt_btwqi(self):
        self.assertEqual(caesarCipher("hello world", 5), "mjqqt btwqi")

    def test_give_reverse_case_k2_should_return_bqwvq_oxyd(self):
        self.assertEqual(caesarCipher("Reverse-Case", 2), "Bqwvq-Oxyd")

    def test_give_large_shift_k52_should_return_same_as_original(self):
        self.assertEqual(caesarCipher("LargeShift", 52), "LargeShift")

    def test_give_special_chars_k4_should_return_same_special_chars(self):
        self.assertEqual(caesarCipher("1234!@#$", 4), "5678!@#$")

    def test_give_negative_shift_k_3_should_return_zab(self):
        self.assertEqual(caesarCipher("abc", -3), "zab")

    def test_give_all_alphabet_k13_should_return_nopqrstuvwxyzabcdefghijklm(self):
        self.assertEqual(caesarCipher("abcdefghijklmnopqrstuvwxyz", 13), "nopqrstuvwxyzabcdefghijklm")
