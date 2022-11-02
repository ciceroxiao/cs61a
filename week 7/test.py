import unittest

from disc06 import add_this_many, filter_iter, is_prime, primes_gen
from homework05 import gen_perms, hailstone, merge, remainders_generator, sequence
from lab06 import count_occurrences, insert_items, repeated


class TestLab06(unittest.TestCase):
    def test_insert_items(self):
        test_lst = [1, 5, 8, 5, 2, 3]
        self.assertEqual(insert_items(test_lst, 5, 7), [1, 5, 7, 8, 5, 7, 2, 3])

        double_lst = [1, 2, 1, 2, 3, 3]
        self.assertEqual(insert_items(double_lst, 3, 4), [1, 2, 1, 2, 3, 4, 3, 4])

        large_lst = [1, 4, 8]
        large_lst2 = insert_items(large_lst, 4, 4)
        self.assertEqual(large_lst2, [1, 4, 4, 8])

        large_lst3 = insert_items(large_lst2, 4, 6)
        self.assertEqual(large_lst3, [1, 4, 6, 4, 6, 8])

        self.assertTrue(large_lst3 is large_lst)

    def test_count_occurrences(self):
        s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
        self.assertEqual(count_occurrences(s, 10, 9), 3)

        s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
        self.assertEqual(count_occurrences(s2, 3, 10), 2)

        s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
        self.assertEqual(count_occurrences(s, 1, 3), 1)
        self.assertEqual(count_occurrences(s, 3, 2), 3)
        self.assertEqual(next(s), 1)

        s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
        self.assertEqual(count_occurrences(s2, 6, 6), 2)

    def test_repeat(self):
        s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
        self.assertEqual(repeated(s, 2), 9)

        s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
        self.assertEqual(repeated(s2, 3), 8)

        s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
        self.assertEqual(repeated(s, 3), 2)
        self.assertEqual(repeated(s, 3), 5)

        s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
        self.assertEqual(repeated(s2, 3), 2)


class TestDisc06(unittest.TestCase):
    def test_add_this_many(self):
        s = [1, 2, 4, 2, 1]
        add_this_many(1, 5, s)
        self.assertEqual(s, [1, 2, 4, 2, 1, 5, 5])

        add_this_many(2, 2, s)
        self.assertEqual(s, [1, 2, 4, 2, 1, 5, 5, 2, 2])

    def test_filter_iter(self):
        is_even = lambda x: x % 2 == 0
        self.assertEqual(list(filter_iter(range(5), is_even)), [0, 2, 4])

        all_odd = (2 * y - 1 for y in range(5))
        self.assertEqual(list(filter_iter(all_odd, is_even)), [])

        naturals = (n for n in range(1, 100))
        s = filter_iter(naturals, is_even)
        self.assertEqual(next(s), 2)
        self.assertEqual(next(s), 4)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(16))
        self.assertTrue(is_prime(521))

    def test_primes_gen(self):
        pg = primes_gen(7)
        self.assertEqual(list(pg), [7, 5, 3, 2])


class TestHomework05(unittest.TestCase):
    def test_merge(self):
        a = sequence(2, 3)
        b = sequence(3, 2)
        result = merge(a, b)
        self.assertEqual(
            [next(result) for _ in range(10)], [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
        )

    def test_gen_perms(self):
        perms = gen_perms([100])
        self.assertEqual(next(perms), [100])
        with self.assertRaises(StopIteration):
            next(perms)

        self.assertEqual(
            sorted(gen_perms([1, 2, 3])),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )

        self.assertEqual(
            sorted(gen_perms((10, 20, 30))),
            [
                [10, 20, 30],
                [10, 30, 20],
                [20, 10, 30],
                [20, 30, 10],
                [30, 10, 20],
                [30, 20, 10],
            ],
        )

        self.assertEqual(sorted(gen_perms("ab")), [["a", "b"], ["b", "a"]])

    def test_hailstone(self):
        hail_gen = hailstone(10)
        self.assertEqual(
            [next(hail_gen) for _ in range(10)], [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
        )
        self.assertEqual(next(hail_gen), 1)

    # 除了 doctest，我暂时还不知道该如何测试有打印行为的函数，因此暂时跳过此测试
    def test_remainders_generator(self):
        import types

        self.assertEqual(
            [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)],
            [True, True, True, True, True],
        )


if __name__ == "__main__":
    unittest.main()
