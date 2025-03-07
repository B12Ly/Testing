from cat_mouse.cat_mouse import cat_and_mouse
import unittest


class CatMouseTest(unittest.TestCase):
    # ตัวอย่างเทสต์เคสจากสไลด์ (หน้า 21)
    def test_give_1_2_3_should_CatB(self):
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")

    def test_give_1_3_2_should_MouseC(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_give_1_5_4_should_CatB(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")

    def test_give_10_20_15_should_MouseC(self):
        self.assertEqual(cat_and_mouse(10, 20, 15), "Mouse C")

    def test_give_0_0_0_should_MouseC(self):
        self.assertEqual(cat_and_mouse(0, 0, 0), "Mouse C")

    def test_give_negative_positions_should_MouseC(self):
        self.assertEqual(cat_and_mouse(-5, -1, -3), "Mouse C")

    def test_give_4_8_5_should_CatA(self):
        self.assertEqual(cat_and_mouse(4, 8, 5), "Cat A")