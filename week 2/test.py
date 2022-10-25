import unittest

from homework import accumulate, product
from lab01 import falling, double_eights
from disc01 import wears_jacket_with_if, is_prime, fizzbuzz, unique_digits, has_digit
from operator import add, mul


class TestHomework(unittest.TestCase):
    def setUp(self):
        self.square = lambda x: x * x
        self.identity = lambda x: x
        self.triple = lambda x: 3 * x
        self.increment = lambda x: x + 1

    def test_product(self):
        self.assertEqual(product(3, self.identity), 6)
        self.assertEqual(product(5, self.identity), 120)
        self.assertEqual(product(3, self.square), 36)
        self.assertEqual(product(5, self.square), 14400)
        self.assertEqual(product(3, self.increment), 24)
        self.assertEqual(product(3, self.triple), 162)

    def test_accumulate(self):
        self.assertEqual(accumulate(add, 0, 5, self.identity), 15)
        self.assertEqual(accumulate(add, 0, 0, self.identity), 0)
        self.assertEqual(accumulate(add, 11, 5, self.identity), 26)
        self.assertEqual(accumulate(add, 11, 0, self.identity), 11)
        self.assertEqual(accumulate(add, 11, 3, self.square), 25)
        self.assertEqual(accumulate(mul, 2, 3, self.square), 72)
        self.assertEqual(accumulate(lambda x, y: x + y + 1, 2, 3, self.square), 19)
        self.assertEqual(accumulate(lambda x, y: 2 * x * y, 2, 3, self.square), 576)
        self.assertEqual(accumulate(lambda x, y: (x + y) % 17, 19, 20, self.square), 16)


class TestLab01(unittest.TestCase):
    def test_falling(self):
        self.assertEqual(falling(6, 3), 120)
        self.assertEqual(falling(4, 3), 24)
        self.assertEqual(falling(4, 1), 4)
        self.assertEqual(falling(4, 0), 1)

    def test_double_eights(self):
        self.assertFalse(double_eights(8))
        self.assertTrue(double_eights(88))
        self.assertTrue(double_eights(2882))
        self.assertTrue(double_eights(880088))
        self.assertFalse(double_eights(12345))
        self.assertFalse(double_eights(80808080))


class TestDisc01(unittest.TestCase):
    def test_wears_jacket_with_if(self):
        self.assertFalse(wears_jacket_with_if(90, False))
        self.assertTrue(wears_jacket_with_if(40, False))
        self.assertTrue(wears_jacket_with_if(100, True))

    def test_is_prime(self):
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(1))

    def test_fizzbuzz(self):
        self.assertIsNone(fizzbuzz(16))

    def test_unique_digits(self):
        self.assertEqual(unique_digits(8675309), 7)
        self.assertEqual(unique_digits(1313131), 2)
        self.assertEqual(unique_digits(13173131), 3)
        self.assertEqual(unique_digits(10000), 2)
        self.assertEqual(unique_digits(101), 2)
        self.assertEqual(unique_digits(10), 2)

    def test_has_digit(self):
        self.assertTrue(has_digit(10, 1))
        self.assertFalse(has_digit(12, 7))
        self.assertTrue(has_digit(1, 1))
        self.assertTrue(has_digit(0, 0))


if __name__ == "__main__":

    unittest.main()
