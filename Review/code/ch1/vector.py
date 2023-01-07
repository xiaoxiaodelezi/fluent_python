#Vector 类
#repr abs add mul

from math import hypot


class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __abs__(self):
        return hypot(self._x, self._y)

    def __repr__(self):
        return 'Vector(%r,%r)' % (self._x, self._y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self._x * scalar, self._y * scalar)


v1 = Vector(1, 2)
print(v1)
print(abs(v1))
print(bool(v1))
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * 10)
