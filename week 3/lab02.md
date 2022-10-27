### Q1: WWPD: Lambda the Free

掌握匿名函数的方法就是将匿名函数改写成普通函数。
改写的过程中，应当要一层一层的改写，以免出现逻辑谬误。

```python
>>> lambda x: x  # A lambda expression with one parameter x
<function ...>

>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
5
# a 可以改写成：
def a(x):
    return x
a(5)

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
3
# 匿名函数不接受参数且此匿名函数永远返回 3
# 此函数可以改写成：
def f():
    return 3

>>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
>>> c = b(88)
>>> c
<funciton ...>

>>> c()
88
# b 可以改写成：
# 1.
def b(x):
    return lambda: x
# 2.
def b(x):
    def f(x=x):
        return x
    return f


>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
16

# d 可以改写成：
def d(f):
    return f(4)


>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
4

# e 可以改写成：
def e(x):
    def f1(y):
        def f2():
            return x + y + z
        return f2
    return f1


>>> f = lambda z: x + z
>>> f(3)
x 未定义

>>> x = None # remember to review the rules of WWPD given above!
>>> x
无输出

# f 可以改写成：
def f(z):
    return x + z


>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
Error，2 是整数，不是函数

>>> higher_order_lambda(g)(2)
4

# higher_order_lambda 可以改写成：
def higher_order_lambda(f):
    def f2(x):
        return f(x)
    return f2


>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
3

# call_thrice 可以改写成：
def call_thrice(f):
    def f2(x):
        return f(f(f(x)))
    return f2

>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda
<function...>

>>> one_thousand = print_lambda(1000)
1000

>>> one_thousand # What did the call to print_lambda return?
无输出，因为 one_thousand 指向 None

# print_lambda 可以改写成：
def print_lambda(z):
    print(z)

```

### Q2: WWPD: Higher Order Functions

```python
>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)
...         return f(x)
...     return odd
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> stewart
<function...>

>>> stewart(61)
61

>>> stewart(-4)
4

>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
beets

>>> chocolate
<function...>

>>> chocolate()
sweets
'cake'

>>> more_chocolate, more_cake = chocolate(), cake
sweets

>>> more_chocolate
'cake'

>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
<function...>

>>> snake(10, 20)()
sweets
'cake'

>>> cake = 'cake'
>>> snake(10, 20)
30
```

### Q3: Lambdas and Currying
见 lab02.py。

### Q4: Count van Count
见 lab02.py。

### Q5: HOF Diagram Practice
pass

### Q6: Composite Identity Function
见 lab02.py。

### Q7: I Heard You Liked Functions...
见 lab02.py。
