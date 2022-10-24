"""此程序包含 week 1 的家庭作业"""
from operator import sub, add


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    # 提供两种方法:
    # 1. 先取出三个数字中较小的两个数字，再计算其平方和
    # return sum([_**2 for _ in sorted([i, j, k])[:2]])
    # 2. 先计算三个数字的平方和，再减去最大的那个数字之平方
    return sum(_**2 for _ in [i, j, k]) - max([i, j, k]) ** 2


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime

    """
    # 此处也提供两个方法
    # 1. 先找出 n 的因数之集合，然后去除其自身，再从因数集合中取出最大值
    # facotrs = set()
    # for i in range(1, n // 2):
    #     if n % i == 0:
    #         facotrs.add(i)
    #         facotrs.add(n / i)
    # facotrs.remove(n)
    # return max(facotrs)

    # 2. 根据每一次除法的结果来确定 n 的最大因数（除了它自身）
    begin_index, the_largest_factor, stop_index = 1, 1, n
    while begin_index < stop_index:
        if n % begin_index == 0:
            the_largest_factor = begin_index
        begin_index += 1
    return the_largest_factor


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)

    steps = 1
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
    return steps
