### Q1: WWPD: Classy Cars

```python
class Car:
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return super().drive()


>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.model
Model S

>>> deneros_car.gas = 10
>>> deneros_car.drive()
Tesla Model S goes vroom!

>>> deneros_car.drive()
Cannot drive!

>>> deneros_car.fill_gas()
Gas level: 20

>>> deneros_car.gas
20

>>> Car.gas
30

>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.wheels = 2
>>> deneros_car.wheels
2

>>> Car.num_wheels
4

>>> deneros_car.drive()
'Cannot drive!'

>>> Car.drive()
TypeError # drive() 缺少参数 self，即实例

>>> Car.drive(deneros_car)
'Cannot drive!'

>>> deneros_car = MonsterTruck('Monster', 'Batmobile')
>>> deneros_car.drive()
Vroom! This Monster Truck is huge!
Monster Batmobile goes vroom!

>>> Car.drive(deneros_car)
Monster Batmobile goes vroom!

>>> MonsterTruck.drive(deneros_car)
Vroom! This Monster Truck is huge!
Monster Batmobile goes vroom!

>>> Car.rev(deneros_car)
AttributeError # 'Car' 没有属性 rev
```

### Q2: Retirement
见 lab07.py 。

### Q3: FreeChecking
见 lab07.py 。

### Q4: Making Cards
见 lab07.py 。

### Q5: Making a Player
见 lab07.py 。

### Q6: AIs: Resourceful Resources
见 lab07.py 。
