# 使用reduce函数和一个匿名函数计算阶乘

from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))
