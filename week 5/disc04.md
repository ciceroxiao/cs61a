### Q1: Count Stair Ways
见 disc04.py 。

### Q2: Count K
见 disc04.py 。

### Q3: WWPD: Lists

```python
>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])

>>>len(a)

>>> 2 in a

>>> a[3][0]
```

### Q4: Even weighted
见 disc04.py 。

### Q5: Max Product
见 disc04.py 。

### Q6: WWPD: Dictionaries

```python
>>> pokemon = {'pikachu': 25, 'dragonair': 148}
>>> pokemon
{'pikachu': 25, 'dragonair': 148}

>>> 'mewtwo' in pokemon
False

>>> len(pokemon)
2

>>> pokemon['mew'] = pokemon['pikachu']
>>> pokemon[25] = 'pikachu'
>>> pokemon
{'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}

>>> pokemon['mewtwo'] = pokemon['mew'] * 2
>>> pokemon
{'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu', 'mewtwo': 50}

>>> pokemon[['firetype', 'flying']] = 146
TypeError
# list 无法做为 dict 的 key，因为 list 可变，不可哈希
```