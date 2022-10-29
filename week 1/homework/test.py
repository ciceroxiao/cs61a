import unittest

from homework_01 import a_plus_abs_b, two_of_three, largest_factor, hailstone


class TestHomework(unittest.TestCase):
    def test_a_plus_abs_b(self):
        self.assertEqual(a_plus_abs_b(2, 3), 5)
        self.assertEqual(a_plus_abs_b(2, -3), 5)
        self.assertEqual(a_plus_abs_b(-1, 4), 3)
        self.assertEqual(a_plus_abs_b(-1, -4), 3)

    def test_two_of_three(self):
        self.assertEqual(two_of_three(1, 2, 3), 5)
        self.assertEqual(two_of_three(5, 3, 1), 10)
        self.assertEqual(two_of_three(10, 2, 8), 68)
        self.assertEqual(two_of_three(5, 5, 5), 50)

    def test_largest_factor(self):
        self.assertEqual(largest_factor(15), 5)
        self.assertEqual(largest_factor(80), 40)
        self.assertEqual(largest_factor(13), 1)

    def test_hailstone(self):
        a = hailstone(10)
        b = hailstone(1)
        self.assertEqual(a, 7)
        self.assertEqual(b, 1)


if __name__ == "__main__":
    unittest.main()
