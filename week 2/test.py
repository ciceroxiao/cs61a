import unittest

from homework import accumulate, product
from solution import falling, double_eights
from operator import add, mul

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1


class TestHomework(unittest.TestCase):
    def test_product(self):
        self.assertEqual(product(3, identity), 6)
        self.assertEqual(product(5, identity), 120)
        self.assertEqual(product(3, square), 36)
        self.assertEqual(product(5, square), 14400)
        self.assertEqual(product(3, increment), 24)
        self.assertEqual(product(3, triple), 162)

    def test_accumulate(self):
        self.assertEqual(accumulate(add, 0, 5, identity), 15)
        self.assertEqual(accumulate(add, 0, 0, identity), 0)
        self.assertEqual(accumulate(add, 11, 5, identity), 26)
        self.assertEqual(accumulate(add, 11, 0, identity), 11)
        self.assertEqual(accumulate(add, 11, 3, square), 25)
        self.assertEqual(accumulate(mul, 2, 3, square), 72)
        self.assertEqual(accumulate(lambda x, y: x + y + 1, 2, 3, square), 19)
        self.assertEqual(accumulate(lambda x, y: 2 * x * y, 2, 3, square), 576)
        self.assertEqual(accumulate(lambda x, y: (x + y) % 17, 19, 20, square), 16)


class TestSolution(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
