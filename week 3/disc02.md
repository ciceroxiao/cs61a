### Q1: Call Diagram
pass

### Q2: Nested Calls Diagrams
pass

### Q3: Lambda the Environment Diagram
pass

### Q4: Make Adder
pass

### Q5: Make Keeper
见 disc02.py。

### Q6: Make Your Own Lambdas

```python
def f1():
    """
    >>> f1()
    3
    """
    return 3


def f2():
    """
    >>> f2()()
    3
    """
    return lambda: 3


def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: x


def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda: lambda x: lambda: x
```

### Q7: Curry2 Diagram
pass

### Q8: Match Maker
见 disc02.py。
