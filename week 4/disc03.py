# Q3: Find the Bug
def skip_mul(n):
    """
    Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)


# Q4: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """

    def f(i):
        if i > (n**0.5):
            return True
        elif n % i == 0:
            return False
        else:
            return f(i + 1)

    return f(2)


# Q5: Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
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

    if n == 1:
        return n
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)


# Q6: Merge Numbers
# 这个方法只能合并已经排序好的数字
def merge(n1, n2):
    """Merges two numbers by digit in decreasing order

    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    # 默认 n1 和 n2 都是已经排序好的数字
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif (n1 % 10) < (n2 % 10):
        return n1 % 10 + merge(n1 // 10, n2) * 10
    else:
        return n2 % 10 + merge(n1, n2 // 10) * 10
