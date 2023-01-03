# 循环引用：b引用a，然后追加到a中，deepcopy会想办法复制a

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

from copy import deepcopy

c = deepcopy(a)
print(c)