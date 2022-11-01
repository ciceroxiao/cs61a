import unittest

from disc05 import (
    balanced,
    count_palindromes,
    find_path,
    height,
    max_path_sum,
    my_filter,
    my_map,
    my_reduce,
    sum_tree,
    tree,
)
from homework_04 import arm, examples, mobile, has_path
import homework_04
from lab05 import flatten


class TestLab05(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4])
        self.assertEqual(flatten([[1, [1, 1]], 1, [1, 1]]), [1, 1, 1, 1, 1, 1])


class TestDisc05(unittest.TestCase):
    def test_my_map(self):
        self.assertEqual(my_map(lambda x: x * x, [1, 2, 3]), [1, 4, 9])

    def test_my_filter(self):
        self.assertEqual(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]), [2, 4])

    def test_my_reduce(self):
        self.assertEqual(my_reduce(lambda x, y: x + y, [1, 2, 3, 4]), 10)
        self.assertEqual(my_reduce(lambda x, y: x * y, [1, 2, 3, 4]), 24)
        self.assertEqual(my_reduce(lambda x, y: x * y, [4]), 4)
        self.assertEqual(my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]), 11)

    def test_count_palindromes(self):
        self.assertEqual(count_palindromes(("Acme", "Madam", "Pivot", "Pip")), 2)
        self.assertEqual(count_palindromes(["101", "rAcECaR", "much", "wow"]), 3)

    def test_height(self):
        t1 = tree(3, [tree(5, [tree(1)]), tree(2)])
        self.assertEqual(height(t1), 2)

        t2 = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
        self.assertEqual(height(t2), 3)

    def test_max_path_sum(self):
        t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
        self.assertEqual(max_path_sum(t), 11)

    def test_find_path(self):
        t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
        self.assertEqual(find_path(t, 5), [2, 7, 6, 5])

    def test_sum_tree(self):
        t = tree(4, [tree(2, [tree(3)]), tree(6)])
        self.assertEqual(sum_tree(t), 15)

    def test_balanced(self):
        t1 = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
        self.assertTrue(balanced(t1))

        t2 = tree(1, [t1, tree(1)])
        self.assertFalse(balanced(t2))

        t3 = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
        self.assertFalse(balanced(t3))


class TestHomewor04(unittest.TestCase):
    def test_balanced(self):
        t, u, v = examples()
        self.assertTrue(homework_04.balanced(t))
        self.assertTrue(homework_04.balanced(v))

        w = mobile(arm(3, t), arm(2, u))
        self.assertFalse(homework_04.balanced(w))
        self.assertFalse(homework_04.balanced(mobile(arm(1, v), arm(1, w))))
        self.assertFalse(homework_04.balanced(mobile(arm(1, w), arm(1, v))))

    def test_has_path(self):
        greetings = tree(
            "h",
            [tree("i"), tree("e", [tree("l", [tree("l", [tree("o")])]), tree("y")])],
        )
        self.assertTrue(has_path(greetings, "h"))
        self.assertFalse(has_path(greetings, "i"))
        self.assertTrue(has_path(greetings, "hi"))
        self.assertTrue(has_path(greetings, "hello"))
        self.assertTrue(has_path(greetings, "hey"))
        self.assertFalse(has_path(greetings, "bye"))
        self.assertFalse(has_path(greetings, "hint"))


if __name__ == "__main__":
    unittest.main()
