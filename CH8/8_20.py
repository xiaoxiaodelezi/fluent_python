# 使用另一个元组构建元组，得到的其实是同一个元组

t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 is t2)
t3 = t1[:]
print(t3 is t1)