### Q1: WWPD: Squared Virahanka Fibonacci

```python
>>> def virfib_sq(n):
>>>     print(n)
>>>     if n <= 1:
>>>         return n
>>>     return (virfib_sq(n - 1) + virfib_sq(n - 2)) ** 2
>>> r0 = virfib_sq(0)
0

>>> r1 = virfib_sq(1)
1

>>> r2 = virfib_sq(2)
2
1
0

>>> r3 = virfib_sq(3)
3
2
1
0
1

>>> r3
4

>>> (r1 + r2) ** 2
4

>>> r4 = virfib_sq(4)
4
3
2
1
0
2
1
0

>>> r4
25
```

### Q2: Summation
见 lab04.py 。

### Q3: Pascal's Triangle
见 lab04.py 。

### Q4: Insect Combinatorics
见 lab04.py 。

### Q5: Couple
见 lab04.py 。

### Q6: Double Eights
见 lab04.py 。

### Q7: Coordinates
见 lab04.py 。

### Q8: Riffle Shuffle
见 lab04.py 。
