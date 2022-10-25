week 2 中 Lab01 的解答

### Q1: Syllabus Quiz
pass

### Q2: WWPD: Control

```python
>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
23

>>> xk(10, 6)
23

>>> xk(4, 6)
6

>>> xk(0, 0)
25

>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothing")
>>> how_big(7)
big

>>> how_big(12)
huge

>>> how_big(1)
small

>>> how_big(-1)
nothing

>>> n = 3
>>> while n >= 0:
...     n -= 1
...     print(n)
2
1
0

>>> positive = 28
>>> while positive:
...    print("positive?")
...    positive -= 3
positive?
positive?
positive?
positive?
positive?
positive?
positive?
positive?
positive?

>>> positive = -9
>>> negative = -12
>>> while negative:
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
-12
-9
-6
```

### Q3: WWPD: Veritasiness

```python
# 记住，Python 中的逻辑操作符是「短路运作符」
>>> True and 13
13

>>> True and 0
0

>>> False and 13
False

>>> False or 0
0

>>> False or True
True

>>> not 10
False

>>> not None
True

>>> True and 1 / 0 and False
DivideError

>>> True or 1 / 0 or False
True

>>> True and 0
0

>>> False or 1
1

>>> 1 and 3 and 6 and 10 and 15
15

>>> 1 and 3 and 0 and 10 and 15
0

>>> -1 and 1 > 0
True

>>> 0 or False or 2 or 1 / 0
2

>>> not 0
True

>>> (1 + 1) and 1
1

>>> 1/0 or True
Error

>>> (True or False) and False
False
```

### Q4: Debugging Quiz
pass

### Q5: Falling Factorial

```python
def falling(n, k):
    """Compute the falling factorial of n to depth k.
    计算 n 的下降阶乘，其下降深度为 k。

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
        result, n = result*n, n-1
    return result
```

### Q6: Sum Digits

```python
def sum_digits(y):
    """Sum all the digits of y.
    计算 y 的所有数字之和。

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
    total = 0
    while y > 0:
        total += y % 10
        y = y // 10
    return total
```

### Q7: WWPD: What If?

```python
>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
10
foo

>>> def bake(cake, make):
...     if cake == 0:
...         cake = cake + 1
...         print(cake)
...     if cake == 1:
...         print(make)
...     else:
...         return cake
...     return make
>>> bake(0, 29)
1
29


>>> bake(1, "mashed potatoes")
mashed potatoes
```

### Q8: Double Eights

```python
def double_eights(n):
    """Return true if n has two eights in a row.
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
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False
```
