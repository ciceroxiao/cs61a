### Q1: WWPD: List-Mutation

```python
>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
无输出

>>> lst
[5, 6, 7, 8, 6]

>>> lst.insert(0, 9)
>>> lst
[9, 5, 6, 7, 8, 6]

>>> x = lst.pop(2)
>>> lst
[9, 5, 7, 8, 6]

>>> lst.remove(x)
>>> lst
[9, 5, 7, 8]

>>> a, b = lst, lst[:]
>>> a is lst
True

>>> b == lst
True

>>> b is lst
False

>>> lst = [1, 2, 3]
>>> lst.extend([4,5])
>>> lst
[1, 2, 3, 4, 5]

>>> lst.extend([lst.append(9), lst.append(10)])
>>> lst
[1, 2, 3, 4, 5, [1, 2, 3, 4, 5, 9], [1, 2, 3, 4, 5, 10]]
```

### Q2: Insert Items
见 lab06.py 。

### Q3: WWPD: Iterators

```python
>>> s = [1, 2, 3, 4]
>>> t = iter(s)
>>> next(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator

>>> next(t)
1

>>> next(t)
2

>>> iter(s)
<list_iterator object at ...> # 返回一个迭代器内存地址

>>> next(iter(s))
1

>>> next(iter(t))
3

>>> next(iter(s))
2

>>> next(iter(t))
4

>>> next(t)
StopIteration


>>> r = range(6)
>>> r_iter = iter(r)
>>> next(r_iter)
0

>>> [x + 1 for x in r]
[1, 2, 3, 4, 5, 6]

>>> [x + 1 for x in r_iter]
[2, 3, 4, 5, 6]

>>> next(r_iter)
StopIteration

>>> list(range(-2, 4))   # Converts an iterable into a list
[-2, -1, 0, 1, 2, 3]

>>> map_iter = map(lambda x : x + 10, range(5))
>>> next(map_iter)
10

>>> next(map_iter)
11

>>> list(map_iter)
[12, 13, 14]

>>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
...     print(e)
1000
1002
1004
1006

>>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
[5, 7, 9]

>>> for e in zip([10, 9, 8], range(3)):
...   print(tuple(map(lambda x: x + 2, e)))
(12, 2)
(11, 3)
(10, 4)
```

### Q4: Count Occurrences
见 lab06.py 。

### Q5: Repeated
见 lab06.py 。

