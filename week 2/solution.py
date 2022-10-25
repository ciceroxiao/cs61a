"""此程序包含 Solution 中的习题"""


def falling(n, k):
    """Compute the falling factorial of n to depth k.
    计算 n 的下降阶乘，其下降深度为 k。

    :param n: 需要计算的值
    :type n: int
    :param k: 计算 n 的下降阶乘时的下降深度
    :type k: int

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    result, stop = 1, n - k
    while n > stop:
        result, n = result * n, n - 1
    return result


def sum_digits(y):
    """Sum all the digits of y.
    计算 y 的所有数字之和。

    :param y: 需要计算的数字
    :type y: int

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    result = 0
    while y > 0:
        result, y = result + y % 10, y // 10
    return result


def double_eights(n):
    """Return true if n has two eights in a row.
    如果整数 n 中有两个连续的 8 ，则返回 True ；否则，返回 False

    :param n: 想要测试的数字
    :type n: int

    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    # 思路：
    # 设置两个变量，first_eight 和 second_eight
    # 在寻找的过程中，不断改变 n、first_eight 和 seconde_eight 的值
    # 如果 first_eight 和 second_eight 都是 True 的话，则整个函数返回 True
    # 如果 n = 0 时仍未出现 first_eight 和 second_eight 都是 True 的话，则返回 False
    first_eight = second_eight = False
    while n > 0:
        second_eight = n % 10 == 8
        if first_eight and second_eight:
            return True
        elif second_eight:
            first_eight = True
        else:
            first_eight = False
        n = n // 10
    return False
