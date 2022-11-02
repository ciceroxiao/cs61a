### Q1: WWPD: Mutability

```python
>>> x = [1, 2, 3]
>>> y = x
>>> x += [4]
>>> x
[1, 2, 3, 4]

>>> y # y is pointing to the same list as x, which got mutated
[1, 2, 3, 4]

>>> x = [1, 2, 3]
>>> y = x
>>> x = x + [4] # creates NEW list, assigns it to x
>>> x
[1, 2, 3, 4]

>>> y   # y still points to OLD list, which was not mutated
[1, 2, 3]

>>> s1 = [1, 2, 3]
>>> s2 = s1
>>> s1 is s2
True

>>> s2.extend([5, 6])
>>> s1[4]
6

>>> s1.append([-1, 0, 1])
>>> s2[5]
[-1, 0, 1]

>>> s3 = s2[:]
>>> s3.insert(3, s2.pop(3))
>>> len(s1)
5

>>> s1[4] is s3[6]
True

>>> s3[s2[4][1]]
1

>>> s1[:3] is s2[:3]
False

>>> s1[:3] == s2[:3]
True

>>> s1[4].append(2)
>>> s3[6][3]
2
```

### Q2: Add This Many
见 disc06.py 。

### Q3: WWPD: Iterators

```python
>>> s = "cs61a"
>>> s_iter = iter(s)
>>> next(s_iter)
c

>>> next(s_iter)
s

>>> list(s_iter)
["6", "1", "a"]

>>> s = [[1, 2, 3, 4]]
>>> i = iter(s)
>>> j = iter(next(i))
>>> next(j)
1

>>> s.append(5)
>>> next(i)
5

>>> next(j)
2

>>> list(j)
[3, 4]
>>> next(i)
StopIteration
```

### Q4: WWPD: Generators

```python
>>> def infinite_generator(n):
...     yield n
...     while True:
...     	n += 1
...     	yield n
>>> next(infinite_generator)
TypeError

>>> gen_obj = infinite_generator(1)
>>> next(gen_obj)
1

>>> next(gen_obj)
2

>>> list(gen_obj)
Infinite Loop
```

### Q5: Filter-Iter
见 disc06.py 。

### Q6: Primes Generator
见 disc06.py 。

### Q7: Generate Preorder
见 disc06.py 。

### Q8: (Optional) Mystery Reverse Environment Diagram
见 disc06.py 。
