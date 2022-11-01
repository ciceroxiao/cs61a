# Q1: Num eights
def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    if pos <= 0:
        return 0
    elif pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    else:
        return num_eights(pos // 10)


# Q2: Ping-pong
# 如果某个数字包含 8 或者是 8 的倍数，就转换方向
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """

    def get_result(i, result, step):
        if i == n:
            return result
        if i % 8 == 0 or num_eights(i) > 0:
            return get_result(i + 1, result - step, -step)
        else:
            return get_result(i + 1, result + step, step)

    return get_result(1, 1, 1)


# Q3: Count coins
def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    else:
        return


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1
    else:
        return


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """

    def get_ways(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0 or smallest_coin is None:
            return 0
        with_smallest_coin = get_ways(
            change=change - smallest_coin, smallest_coin=smallest_coin
        )
        without_smallest_coin = get_ways(
            change=change, smallest_coin=next_larger_coin(smallest_coin)
        )
        return with_smallest_coin + without_smallest_coin

    return get_ways(change=change, smallest_coin=1)


# Q4: Busy Beaver Contest
# 放弃
anonymous = False


def beaver(f):
    pass
