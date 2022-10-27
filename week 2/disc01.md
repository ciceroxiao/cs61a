### Q1: Case Conundrum

```python
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

special_case()
12

def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

just_in_case()
19

def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

case_in_point()
12
```

### Q2: Jacket Weather?
见 disc01.py。


### Q3: Square So Slow

```python
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))
没有输出，因为此段代码陷入无限循环
```

### Q4: Is Prime?
见 disc01.py。

### Q5: Fizzbuzz
见 disc01.py。

### Q6: Unique Digits
见 disc01.py。