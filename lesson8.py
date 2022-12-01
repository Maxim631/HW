import datetime
import time


class Auto:
    def __init__(self, brand, mark, age, color, weight):
        self.brand: str = brand
        self.age: int = age
        self.color: str = color
        self.mark: str = mark
        self.weight: float = weight

    def move(self):
        return f'{self.brand} {self.mark} {self.age} move'

    def stop(self):
        return f'{self.brand} {self.mark} {self.age} stop'

    def birthday(self):
        self.age += 1
        return f'{self.brand} {self.mark} {self.age}'


class Truck(Auto):
    def __init__(self, brand, mark, age, color, weight, max_load):
        super().__init__(brand, mark, age, color, weight)
        self.max_load: float = max_load

    def move(self):
        return f'Attention {self.brand} {self.mark} {self.age} move'

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, mark, age, color, weight, max_speed):
        super().__init__(brand, mark, age, color, weight)
        self.max_speed: int = max_speed

    def move(self):
        return f'{self.brand} {self.mark} {self.age} move max speed is {self.max_speed}'


# truck1 = Truck('MB', 'Actros', 2, 'white', 8.7, 18)
# car1 = Auto('vw', 'golf', 24, 'red', 1.2)


class Point:

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)


class Circle(Point):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius: int  = radius

    def __str__(self):
        return f'{self.x},{self.y},{self.radius}'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(x, y, radius) if radius else Point(x, y)



