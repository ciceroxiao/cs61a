import unittest

from disc03 import skip_mul, is_prime, hailstone, merge
from homework import num_eights, pingpong, next_smaller_coin, next_larger_coin
from homework import count_coins


class TestDisc03(unittest.TestCase):
    def test_skip_mul(self):
        self.assertEqual(skip_mul(5), 15)
        self.assertEqual(skip_mul(8), 384)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(16))
        self.assertTrue(is_prime(521))

    def test_hailstone(self):
        self.assertEqual(hailstone(10), 7)
        self.assertEqual(hailstone(1), 1)

    def test_merge(self):
        self.assertEqual(merge(31, 42), 4321)
        self.assertEqual(merge(21, 0), 21)
        self.assertEqual(merge(21, 31), 3211)


class TestHomework(unittest.TestCase):
    def test_num_eights(self):
        self.assertEqual(num_eights(3), 0)
        self.assertEqual(num_eights(8), 1)
        self.assertEqual(num_eights(888_8888_8), 8)
        self.assertEqual(num_eights(2638), 1)
        self.assertEqual(num_eights(863_80), 2)
        self.assertEqual(num_eights(123_45), 0)
        self.assertEqual(num_eights(878_2089), 3)

    def test_pingpong(self):
        self.assertEqual(pingpong(8), 8)
        self.assertEqual(pingpong(10), 6)
        self.assertEqual(pingpong(15), 1)
        self.assertEqual(pingpong(21), -1)
        self.assertEqual(pingpong(22), -2)
        self.assertEqual(pingpong(30), -2)
        self.assertEqual(pingpong(68), 0)
        self.assertEqual(pingpong(69), -1)
        self.assertEqual(pingpong(80), 0)
        self.assertEqual(pingpong(81), 1)
        self.assertEqual(pingpong(82), 0)
        self.assertEqual(pingpong(100), -6)

    def test_next_smaller_coin(self):
        self.assertEqual(next_smaller_coin(25), 10)
        self.assertEqual(next_smaller_coin(10), 5)
        self.assertEqual(next_smaller_coin(5), 1)
        self.assertIsNone(next_smaller_coin(2))

    def test_next_larger_coin(self):
        self.assertEqual(next_larger_coin(1), 5)
        self.assertEqual(next_larger_coin(5), 10)
        self.assertEqual(next_larger_coin(10), 25)
        self.assertIsNone(next_larger_coin(25))

    def test_count_coins(self):
        self.assertEqual(count_coins(1), 1)
        self.assertEqual(count_coins(2), 1)
        self.assertEqual(count_coins(15), 6)
        self.assertEqual(count_coins(10), 4)
        self.assertEqual(count_coins(20), 9)
        self.assertEqual(count_coins(100), 242)
        self.assertEqual(count_coins(200), 1463)


if __name__ == "__main__":
    unittest.main()
