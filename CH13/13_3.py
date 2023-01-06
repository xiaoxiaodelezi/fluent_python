# 一元运算符+得到一个新Counter实例，但是没有零值和负值计数器

from collections import Counter

ct = Counter('abracadabra')
print(ct)
ct['r'] = -3
ct['d'] = 0
print(ct)
print(+ct)