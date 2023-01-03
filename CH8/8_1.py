# 变量a和变量b引用同一个列表，而不是那个列表的副本

a = [1, 2, 3]
b = a
a.append(4)
print(b)