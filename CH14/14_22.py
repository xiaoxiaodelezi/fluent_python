# itertools.tee 函数产生多个生成器，每个生成器都可以产出输入的各个元素

import itertools

print(list(itertools.tee('ABC')))
g1, g2 = itertools.tee('ABC')
print(next(g1))
print(next(g2))
print(next(g2))
print(list(g1))
print(list(g2))
print(list(zip(*itertools.tee('ABC'))))