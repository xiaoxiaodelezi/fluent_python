# 组合学生成器函数会从输入的各个元素中产生多个值

import itertools

print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations_with_replacement('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.product('ABC', repeat=2)))
