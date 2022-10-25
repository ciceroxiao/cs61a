def product(n: int, tern) -> int:
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    # 根据函数的定义可知，其需求是：给予一个正整数 n 和一个纯函数 tern，使用
    #   纯函数 tern 来逐个处理 1~n，最后返回 tern 处理后的累计值。
    #   此纯函数 tern 只接收一个参数，并返回一个值。
    #
    # 具体案例： product(5, identity)，其计算过程是：
    #   1 --> 1 * 2 --> 1 * 2 * 3 --> 1 * 2 * 3 * 4 --> 1 * 2 * 3 *4
    #   --> 1 * 2 * 3 * 4 * 5
    #
    # 实现思路：使用 while 来迭代实现需求
    result, start = 1, 1
    while start <= n:
        result = result * tern(start)
        start += 1
    return result


def accumulate(merger, start: int, n: int, term) -> int:
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    n: a positive integer
    term:  a function that takes one argument to produce the term
    merger: a two-argument function that specifies how the current term is
            merged with the previously accumulated terms
    start: value at which to start the accumulation

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    # 根据函数定义可知，其需求是：给定一个正整数 n 和纯函数 tern，先使用 tern 处理 1~n。
    #   然后，再给定一个起始数字 start 和纯函数 merger
    #
    # 观察最后几个 lambda 函数可知，例如 accumulate(mul, 2, 3, square)
    # 其计算过程是：
    # start --> start * 1^2 --> start * 1^2 * 2^2 --> start * 1^2 * 2^2 * 3^2
    # 实现思路：
    result, start_num = start, 1
    while start_num <= n:
        result = merger(term(start_num), result)
        start_num += 1
    return result
