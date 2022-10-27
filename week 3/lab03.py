# Q1: Ordered Digits
def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    如果正整数 n （基数为 10 ）以非递减顺序排列，则返回 True ；否则返回 False 。

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    while x > 10:
        first_num, second_num = x % 10, (x // 10) % 10
        if first_num < second_num:
            return False
        x = x // 10
    return True


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:
        while (n % 10) > (n // 10) % 10 and n > 10:
            n = n // 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


# Q3: Make Repeater
def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """

    def repeater(x):
        i = 0
        while i < n:
            x, i = func(x), i + 1
        return x

    return repeater


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""

    def f(x):
        return func1(func2(x))

    return f


# Q4: Apply Twice
def apply_twice(func):
    """Return a function that applies func twice


    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    return make_repeater(func, 2)


# Q5: It's Always a Good Prime
# TODO:
def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = 2
    while i < n:
        if not checker(i):
            checker = (lambda f, i: lambda x: x % i == 0 or f(x))(checker, i)
        i = i + 1
    return checker


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """

    def checker(x):
        return False

    i = 2
    while i <= n:
        if not checker(i):

            def outer(f, i):
                def inner(x):
                    return x % i == 0 or f(x)

                return inner

            # 每一次循环，checker 所指向的内存地址都会变动
            # 也就是说，每一次循环后， checker 的「定义」都会变动
            checker = outer(checker, i)

        i = i + 1
    return checker


# Q6: Church numerals
# TODO:
def zero(f):
    def f2(x):
        return x

    return f2


def successor(n):
    def f3(func):
        def f4(x):
            return func(n(func)(x))

        return f4

    return f3
