### Q1: Warm Up: Recursive Multiplication

如果两个输入的某一个为 1 ，则直接返回另一个输入。

`multiply(m - 1, n)` 和 `multiply(m, n - 1)` 的输出结果相同，但是 `multiply(m, n - 1)` 才是本题的解法。

```python
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)
```

### Q2: Recursion Environment Diagram

rec(3, 2) --> 9
rec(3, 2) --> 3 * rec(3, 1) --> 3 * 3 * 1 --> 9

### Q3: Find the Bug
见 disc03.py 。

### Q4: Is Prime
见 disc03.py 。

### Q5: Recursive Hailstone
见 disc03.py 。

### Q6: Merge Numbers
见 disc03.py 。
