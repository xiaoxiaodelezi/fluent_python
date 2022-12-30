# 使用partia把一两个参数函数改编成需要单参数的可调用对象
from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))
