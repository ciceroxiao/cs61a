import unittest

from lab02 import lambda_curry2, count_factors, count_primes, is_prime
from lab02 import count_cond, composer, composite_identity, cycle
from disc02 import make_keeper, match_k
from lab03 import ordered_digits, get_k_run_starter, make_repeater
from lab03 import apply_twice, div_by_primes_under, div_by_primes_under_no_lambda


class TestLab02(unittest.TestCase):
    def test_lambda_curry2(self):
        from operator import add, mul, mod

        curried_add = lambda_curry2(add)
        add_three = curried_add(3)
        self.assertEqual(add_three(5), 8)

        curried_mul = lambda_curry2(mul)
        mul_5 = curried_mul(5)
        self.assertEqual(mul_5(42), 210)

        self.assertEqual(lambda_curry2(mod)(123)(10), 3)

    def test_count_factors(self):
        self.assertEqual(count_factors(6), 4)
        self.assertEqual(count_factors(4), 3)

    def test_count_primes(self):
        self.assertEqual(count_primes(6), 3)
        self.assertEqual(count_primes(13), 6)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(15))

    def test_count_cond(self):
        count_factors = count_cond(lambda n, i: n % i == 0)
        self.assertEqual(count_factors(2), 2)
        self.assertEqual(count_factors(4), 3)
        self.assertEqual(count_factors(12), 6)

        is_prime = lambda n, i: count_factors(i) == 2
        count_primes = count_cond(is_prime)
        self.assertEqual(count_primes(2), 1)
        self.assertEqual(count_primes(3), 2)
        self.assertEqual(count_primes(4), 2)
        self.assertEqual(count_primes(5), 3)
        self.assertEqual(count_primes(20), 8)

    def test_composer(self):
        a1 = composer(lambda x: x**2, lambda x: x + 1)
        self.assertEqual(a1(4), 25)

        a2 = composer(lambda x: x * 3, a1)
        self.assertEqual(a2(4), 75)
        self.assertEqual(a2(5), 108)

    def test_composite_identity(self):
        b1 = composite_identity(lambda x: x**2, lambda x: x + 1)
        self.assertTrue(b1(0))
        self.assertFalse(b1(4))

    def test_cycle(self):
        my_cycle = cycle(lambda x: x + 1, lambda x: x * 2, lambda x: x + 3)

        identity = my_cycle(0)
        self.assertEqual(identity(5), 5)

        add_one_then_double = my_cycle(2)
        self.assertEqual(add_one_then_double(1), 4)

        do_all_functions = my_cycle(3)
        self.assertEqual(do_all_functions(2), 9)

        do_more_than_a_cycle = my_cycle(4)
        self.assertEqual(do_more_than_a_cycle(2), 10)

        do_two_cycles = my_cycle(6)
        self.assertEqual(do_two_cycles(1), 19)


class TestDisc02(unittest.TestCase):
    def test_make_keeper(self):
        def is_even(x):
            return x % 2 == 0

        self.assertIsNone(make_keeper(5)(is_even))

    def test_mathc_k(self):
        self.assertTrue(match_k(2)(1010))
        self.assertFalse(match_k(2)(2010))
        self.assertFalse(match_k(1)(1010))
        self.assertTrue(match_k(1)(1))
        self.assertFalse(match_k(1)(211111111111))
        self.assertTrue(match_k(3)(123123))
        self.assertFalse(match_k(2)(123123))


class TestLab03(unittest.TestCase):
    def test_ordered_digits(self):
        self.assertTrue(ordered_digits(5))
        self.assertTrue(ordered_digits(11))
        self.assertTrue(ordered_digits(123))
        self.assertTrue(ordered_digits(1357))
        self.assertFalse(ordered_digits(21))

        result = ordered_digits(1375)
        self.assertFalse(result)

    def test_get_k_run_starter(self):
        self.assertEqual(get_k_run_starter(123444345, 0), 3)
        self.assertEqual(get_k_run_starter(123444345, 1), 4)
        self.assertEqual(get_k_run_starter(123444345, 2), 4)
        self.assertEqual(get_k_run_starter(123444345, 3), 1)
        self.assertEqual(get_k_run_starter(123412341234, 1), 1)
        self.assertEqual(get_k_run_starter(1234234534564567, 0), 4)
        self.assertEqual(get_k_run_starter(1234234534564567, 1), 3)
        self.assertEqual(get_k_run_starter(1234234534564567, 2), 2)

    def test_make_repeater(self):
        square = lambda x: x * x
        triple = lambda x: 3 * x
        increment = lambda x: x + 1

        add_three = make_repeater(increment, 3)
        self.assertEqual(add_three(5), 8)

        self.assertEqual(make_repeater(triple, 5)(1), 243)
        self.assertEqual(make_repeater(square, 2)(5), 625)
        self.assertEqual(make_repeater(square, 4)(5), 152_587_890_625)
        self.assertEqual(make_repeater(square, 0)(5), 5)

    def test_apply_twice(self):
        square = lambda x: x * x

        self.assertEqual(apply_twice(square)(2), 16)

    # TODO
    @unittest.skip("看不懂题目和标准答案，因此跳过测试")
    def test_div_by_primes_under(self):
        self.assertFalse(div_by_primes_under(10)(11))
        self.assertFalse(div_by_primes_under(10)(121))
        self.assertTrue(div_by_primes_under(10)(12))
        self.assertFalse(div_by_primes_under(5)(1))

    # TODO
    @unittest.skip("看不懂题目和标准答案，因此跳过测试")
    def test_div_by_primes_under_no_lambda(self):
        self.assertFalse(div_by_primes_under_no_lambda(10)(11))
        self.assertFalse(div_by_primes_under_no_lambda(10)(121))
        self.assertTrue(div_by_primes_under_no_lambda(10)(12))
        self.assertFalse(div_by_primes_under_no_lambda(5)(1))


if __name__ == "__main__":
    unittest.main()
