"""此程序包含 week 2 中 Disc 01 中的习题"""


def wears_jacket_with_if(temp: int, raining: bool) -> bool:
    """如果 temp 小于 50 或者 raining 为 True ，函数返回 True ；否则，返回 False

    :param temp: 外界温度
    :type temp: int
    :param raining: 是否下雨
    :type raining: bool
    :return: bool

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False


def is_prime(n: int) -> bool:
    """如果正整数 n 是素数，则返回 True ；否则，返回 False

    :param n: 需要检验的正整数
    :type n: 正整数
    :return: bool

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False
    start, end = 2, n // 2
    while start <= end:
        if n % start == 0:
            return False
        start += 1
    return True


def fizzbuzz(n: int) -> None:
    """为 1 到 n 的每个数字打印出一条语句，其打印规则如下：
    - 如果该数字仅仅只能被 3 整除，则打印 "fizz"
    - 如果该数字仅仅只能被 5 整除，则打印 "buzz"
    - 如果该数字既能被 3 整除，又能被 5 整除，则打印 "fizzbuzz"
    - 否则，打印数字本身

    :param n:
    :type n: int

    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    print(n)
    return


def unique_digits(n: int) -> int:
    """返回某个数字中唯一数字的数量。

    Args:
        n (int): 想要查询的正整数

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    # new_n = n % 10
    # num_of_unique, nth_of_10 = 1, 1
    # while n > 0:
    #     last_num = n % 10
    #     if not has_digit(new_n, last_num):
    #         num_of_unique += 1
    #     new_n = new_n + last_num * 10**nth_of_10
    #     n, nth_of_10 = n // 10, nth_of_10 + 1
    # return num_of_unique
    # 留下自己的笨拙答案以警醒自己

    # 标准方法：标准方法确实优雅简单且易懂。
    num_of_unique = 0
    for i in range(10):
        if has_digit(n, i):
            num_of_unique += 1
    return num_of_unique


def has_digit(n: int, k: int) -> bool:
    """判断 k 是否是 n 中的数字。

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    if n == k:
        return True
    while n > 0:
        last_num, n = n % 10, n // 10
        if last_num == k:
            return True
    return False
