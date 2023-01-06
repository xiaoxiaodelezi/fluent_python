# 查看几个类的mro属性

print(bool.__mro__)


def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))


print_mro(bool)

import numbers

print_mro(numbers.Integral)

import io

print_mro(io.BytesIO)
print_mro(io.TextIOWrapper)
