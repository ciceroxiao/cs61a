from itertools import count
import unittest

from lab04 import summation, pascal, paths, couple, coords, riffle
from disc04 import count_stair_ways, count_k, even_weighted, max_product


class TestLab04(unittest.TestCase):
    def test_summation(self):
        self.assertEqual(summation(5, lambda x: x * x * x), 225)
        self.assertEqual(summation(9, lambda x: x + 1), 54)
        self.assertEqual(summation(5, lambda x: 2**x), 62)

    def test_pascal(self):
        self.assertEqual(pascal(0, 0), 1)

    def test_paths(self):
        self.assertEqual(paths(2, 2), 2)

    def test_couple(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        self.assertEqual(couple(a, b), [[1, 4], [2, 5], [3, 6]])

        c = ["c", 6]
        d = ["s", "1"]
        self.assertEqual(couple(c, d), [["c", "s"], [6, "1"]])

    def test_coords(self):
        seq = [-4, -2, 0, 1, 3]
        fn = lambda x: x**2
        self.assertEqual(coords(fn, seq, 1, 9), [[-2, 4], [1, 1], [3, 9]])

    def test_riffle(self):
        self.assertEqual(riffle([3, 4, 5, 6]), [3, 5, 4, 6])
        self.assertEqual(
            riffle(range(20)),
            [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19],
        )


class TestDisc04(unittest.TestCase):
    def test_count_stair_ways(self):
        self.assertEqual(count_stair_ways(4), 5)

    def test_count_k(self):
        self.assertEqual(count_k(3, 3), 4)
        self.assertEqual(count_k(4, 4), 8)
        self.assertEqual(count_k(10, 3), 274)
        self.assertEqual(count_k(300, 1), 1)

    def test_even_weighted(self):
        self.assertEqual(even_weighted([1, 2, 3, 4, 5, 6]), [0, 6, 20])

    def test_max_product(self):
        self.assertEqual(max_product([10, 3, 1, 9, 2]), 90)
        self.assertEqual(max_product([5, 10, 5, 10, 5]), 125)
        self.assertEqual(max_product([]), 1)


if __name__ == "__main__":
    unittest.main()
