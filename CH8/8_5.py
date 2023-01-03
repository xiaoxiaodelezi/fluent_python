# 一开始，t1和t2相等，但是修改t1中的一个人可变元素后，两者就不想等了

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)

print(id(t1[-1]))

t1[-1].append(99)
print(t1)

print(id(t1[-1]))

print(t1 == t2)
